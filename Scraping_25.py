# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 18:06:13 2021

@author: mgkog

This code had been wrote to execute contents below.
+ browse web site and get HTML texts
+ output HTML texts as Excel
"""

import requests
from bs4 import BeautifulSoup as BS
import pandas as pd
import datetime

#Define Functions
#Web Scraping
def Scraping(url, parser):
    site = requests.get(url)
    site.encoding = "shift_jis"
    data = BS(site.text, parser)
    return data.find_all(text=True)

#Create File Path
def FilePath(direct_name, file_type):
    dt_now = datetime.datetime.now()
    file_time = dt_now.strftime("%m%d%H%M")
    return direct_name + "KAGAWA_rain_" + file_time + file_type

#Split and Output
def Output(texts, file_path):
    text_list = []
    for text in texts:
        if text.strip():
            text_list.append(text.strip())

    df1 = pd.DataFrame(text_list)
    df1.to_excel(file_path, header=None, index=None)
