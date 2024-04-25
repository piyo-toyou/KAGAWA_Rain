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
    sorted_file_list = sorted(file_list, key=os.path.getctime)

    n = data_number
    if len(sorted_file_list) > n:
        del sorted_file_list[:-n]
    else:
        pass

    df_dict = {}
    for i in range(len(sorted_file_list)):
        df_dict[i] = pd.read_excel(sorted_file_list[i])
    return len(sorted_file_list), df_dict

#Edit Dataframe
def EditDataframe(list_length, df_dict):
    #Index
    out_index = ["久礼・時間","九礼・連続","窪川・時間","窪川・連続"\
        ,"佐賀・時間","佐賀・連続","右山・時間","右山・連続"\
        ,"山奈・時間","山奈・連続","宿毛・時間","宿毛・連続"]
    #Column
    out_column= []
    for i in range(list_length):
        out_column.append(df_dict[i].iloc[3,0] + df_dict[i].iloc[4,0])
    #Array
    df2_array = np.array(())
    get_data_list = np.array([6,7,11,12,16,17,21,22,26,27,31,32])
    for i in range(list_length):
        data_arr = df_dict[i].iloc[get_data_list, [0]].values
        for j in range(len(data_arr)):
            try:
                data_arr[j,0] = float(re.sub("\D", "", data_arr[j,0]))
            except:
                data_arr[j,0] = np.nan
        if df2_array.size > 0:
            df2_array = np.hstack([df2_array, data_arr])
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
    #Fixing Column
    my_sheet.freeze_panes = "B1"
    #Cells width Extension
    for col in my_sheet.columns:
        column = col[0].column_letter
        if column == "A":
            my_sheet.column_dimensions[column].width = 10.00
        else:
            my_sheet.column_dimensions[column].width = 26.00
    #Save Excel
    my_wb.save(output_file)


#Execution
file_path = "C:/Users/S2212357/Documents/Z6_DataBase/Nakamura_Rain_Excel/nakamura_rain_*.xlsx"
list_length, df_dict = InputData(file_path, 50)

df2 = EditDataframe(list_length, df_dict)

output_file = "G:/マイドライブ/Nakamura_Rain/Nakamura_Rain.xlsx"
OutputExcel(df2, output_file)
AdjustExcel(output_file)
