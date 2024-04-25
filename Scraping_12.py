# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 18:06:13 2021

@author: mgkog
"""

from pandas.core.indexes.base import Index
import requests
from bs4 import BeautifulSoup as BS
import pandas as pd
import datetime

#Web Scraping
site = requests.get("http://www.skr.mlit.go.jp/road/mobile/M0711_39_56_0_5_1.html")
data = BS(site.content, "html.parser")
all_text = data.find_all(text=True)

#Output Parameters
dt_now = datetime.datetime.now()
file_time = str(dt_now.month) + str(dt_now.day) + \
     str(dt_now.hour) + str(dt_now.minute)
file_path = "C:/Users/S2212357/Documents/Z6_DataBase/Nakamura_Rain_Excel/nakamura_rain_" + file_time + ".xlsx"

text_list = []
for text in all_text:
    if text.strip():
        text_list.append(text.strip())

df1 = pd.DataFrame(text_list)
df1.to_excel(file_path, header=None, index=None)
