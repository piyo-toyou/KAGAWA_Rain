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

#Define Functions
#Web Scraping
def Scraping(url, parser):
    site = requests.get(url)
    data = BS(site.content, parser)
    return data.find_all(text=True)

#Create File Path
def FilePath(direct_name, file_type):
    dt_now = datetime.datetime.now()
    file_time = str(dt_now.month) + str(dt_now.day) + \
        str(dt_now.hour) + str(dt_now.minute)
    return direct_name + "nakamura_rain_" + file_time + file_type

#Split and Output
def Output(texts, file_path):
    text_list = []
    for text in texts:
        if text.strip():
            text_list.append(text.strip())

    df1 = pd.DataFrame(text_list)
    df1.to_excel(file_path, header=None, index=None)


#Execution
my_url = "http://www.skr.mlit.go.jp/road/mobile/M0711_39_56_0_5_1.html"
my_parser = "html.parser"
all_text = Scraping(my_url, my_parser)

my_directiry = "C:/Users/S2212357/Documents/Z6_DataBase/Nakamura_Rain_Excel/"
file_type = ".xlsx"
file_path = FilePath(my_directiry, file_type)

Output(all_text, file_path)