from numpy.lib.function_base import copy
import pandas as pd
import numpy as np
import glob, os, re

#Input Data
file_path = "C:/Users/S2212357/Documents/Z6_DataBase/Nakamura_Rain_Excel/nakamura_rain_*.xlsx"
file_list = glob.glob(file_path)
sorted_file_list = sorted(file_list, key=os.path.getctime)

#Create Dictionary
df_dict = {}
for i in range(len(sorted_file_list)):
    df_dict[i] = pd.read_excel(sorted_file_list[i])

#Edit Dataframe
#Index
df2_index = ["久礼・時間","九礼・連続","窪川・時間","窪川・連続"\
    ,"佐賀・時間","佐賀・連続","右山・時間","右山・連続"\
        ,"山奈町・時間","山奈町・連続","宿毛・時間","宿毛・連続"]
#Column
df2_column= []
for i in range(len(sorted_file_list)):
    df2_column.append(df_dict[i].iloc[3,0] + df_dict[i].iloc[4,0])
#Array
df2_array = np.array(())
get_data_list = np.array([6,7,11,12,16,17,21,22,26,27,31,32])
for i in range(len(df2_column)):
    data_arr = df_dict[i].iloc[get_data_list, [0]].values
    for j in range(len(data_arr)):
        data_arr[j,0] = float(re.sub("\D", "", data_arr[j,0]))
    if df2_array.size > 0:
        df2_array = np.hstack([df2_array, data_arr])
    else:
        df2_array = data_arr

#Combine Dataframes
df2 = pd.DataFrame(df2_array, df2_index, df2_column)

#Output Excel
output_file = "G:/マイドライブ/Nakamura_Rain/Nakamura_Rain.xlsx"
df2.to_excel(output_file)

#Adjust Excel
import openpyxl
my_wb = openpyxl.load_workbook(output_file)
my_sheet = my_wb.worksheets[0]
#Fixing Column
my_sheet.freeze_panes = "B1"
#Cells width Extension
for col in my_sheet.columns:
    column = col[0].column_letter
    if column == "A":
        my_sheet.column_dimensions[column].width = 15.00
    else:
        my_sheet.column_dimensions[column].width = 26.00
#Save Excel
my_wb.save(output_file)
