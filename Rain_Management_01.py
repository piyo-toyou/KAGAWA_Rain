from numpy.lib.function_base import copy
import pandas as pd
import numpy as np
import glob, os, re

#Input Data
file_path = "C:/Users/S2212357/Desktop/csv/nakamura_rain_*.xlsx"
file_list = glob.glob(file_path)
sorted_file_list = sorted(file_list, key=os.path.getctime)

#Create Dictionary
df_dict = {}
for i in range(len(sorted_file_list)):
    df_dict[i] = pd.read_excel(sorted_file_list[i])

#Edit Dataframe
#Index
df2_index = ["久礼 時間","九礼 連続","窪川 時間","窪川 連続"\
    ,"小黒川 時間","小黒川 連続","右山 時間","右山 連続"\
        ,"山奈町 時間","山奈町 連続","大谷山 連続","大谷山 連続"]
#Column
df2_column= []
for i in range(len(sorted_file_list)):
    df2_column.append(df_dict[i].iloc[3,0] + df_dict[i].iloc[4,0])
#Array
df2_array = np.array(())
get_Jikan_list = np.array([6,11,16,21,26,31])
get_Renzoku_list = np.array([7,12,17,22,27,32])
for i in range(len(df2_column)):
    jikan_arr = df_dict[i].iloc[get_Jikan_list, [0]].values
    renzoku_arr= df_dict[i].iloc[get_Renzoku_list, [0]].values
    for j in range(len(jikan_arr)):
        jikan_arr[j,0] = float(re.sub("\D", "", jikan_arr[j,0]))
        renzoku_arr[j,0] = float(re.sub("\D", "", renzoku_arr[j,0]))
    if df2_array.size > 0:
        df2_array = np.vstack([df2_array, np.squeeze(jikan_arr)])
        df2_array = np.vstack([df2_array, np.squeeze(renzoku_arr)])
    else:
        df2_array = np.vstack([np.squeeze(jikan_arr),np.squeeze(renzoku_arr)])

#Combine Dataframes
df2 = pd.DataFrame(df2_array, df2_index, df2_column)

#Output Excel
df2.to_excel("G:/マイドライブ/Nakamura_Rain/a.xlsx")