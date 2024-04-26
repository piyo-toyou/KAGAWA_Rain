# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 18:06:13 2021

@author: mgkog

This code had been wrote to execute contents below.
+ store Excel files into a dictionary
+ 
"""

#Import Modules
from numpy.lib.function_base import copy
import pandas as pd
import numpy as np
import glob, os, re

#Define Functions
#Input Data
def InputData(file_path, data_number):
    file_list = glob.glob(file_path)
    sorted_file_list = sorted(file_list, key=os.path.getctime, reverse=True)

    n = data_number
    if len(sorted_file_list) > n:
        del sorted_file_list[n:]
    else:
        pass

    df_dict = {}
    for i in range(len(sorted_file_list)):
        df_dict[i] = pd.read_excel(sorted_file_list[i])
    return len(sorted_file_list), df_dict

#Edit Dataframe
def EditDataframe(list_length, df_dict):
    #Column
    out_column = ["時間","連続","時間","連続","時間","連続","時間","連続"]
    #Index
    out_index= []
    for i in range(list_length):
        out_index.append(df_dict[i].iloc[3,0] + df_dict[i].iloc[4,0])
    #Array
    df2_array = np.array(())
    get_data_list = np.array([6,7,11,12,16,17,23,24])
    for i in range(list_length):
        data_arr = np.array(())
        n = 0
        for j in get_data_list:
            data_temp = df_dict[i].iloc[j+n, [0]].values
            try:
                data_arr_temp = float(re.sub("\D", "", data_temp[0]))
            except ValueError:
                if "故障" in data_temp[0]:
                    data_arr_temp = np.nan
                else:
                    data_temp = df_dict[i].iloc[j+n+1, [0]].values
                    data_arr_temp = float(re.sub("\D", "", data_temp[0]))
                    n += 2
            except:
                data_arr_temp = np.nan
            data_arr = np.append(data_arr, data_arr_temp)
        #data_arr = data_arr.reshape(-1,1)
        if df2_array.size > 0:
            df2_array = np.vstack([df2_array, data_arr])
        else:
            df2_array = data_arr
    
    #Combine Dataframes
    return pd.DataFrame(df2_array, out_index, out_column)

#Output Excel
def OutputExcel(df, output_file):
    df.to_excel(output_file)

#Adjust Excel
def AdjustExcel(output_file):
    import openpyxl
    my_wb = openpyxl.load_workbook(output_file)
    my_sheet = my_wb.worksheets[0]
    #Add Spot Name Column
    my_sheet.insert_rows(1)
    spot_name = ["東かがわ", "高松", "観音寺", "財田"]
    col_name = ["B", "D", "F", "H"]
    for i, j in zip(col_name, spot_name):
        my_sheet[i + "1"] = j
    #Fixing Column
    my_sheet.freeze_panes = "A3"
    #Cells width Extension
    for col in my_sheet.columns:
        column = col[0].column_letter
        if column == "A":
            my_sheet.column_dimensions[column].width = 26.00
        else:
            my_sheet.column_dimensions[column].width = 7.00
    #Save Excel
    my_wb.save(output_file)
