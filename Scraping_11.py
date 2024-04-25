# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 18:06:13 2021

@author: mgkog
"""

import requests
from bs4 import BeautifulSoup as BS
import csv
import datetime

#Web Scrayping
site = requests.get("http://www.skr.mlit.go.jp/road/mobile/M0711_39_56_0_5_1.html")
data = BS(site.text, "html.parser")
all_text = data.find("body").get_text()

#Output Parameters
dt_now = datetime.datetime.now()
file_time = str(dt_now.month) + str(dt_now.day) + \
     str(dt_now.hour) + str(dt_now.minute)
file_path = "C:/Users/S2212357/Desktop/csv/nakamura_rain" + file_time + ".csv"

with open(file_path, "w") as f:
    writer = csv.writer(f)
    for text in all_text:
        if text.strip():
            writer.writerow(str(text))