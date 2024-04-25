# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 18:06:13 2021

@author: mgkog
"""

import requests
from bs4 import BeautifulSoup as BS

site = requests.get("http://www.skr.mlit.go.jp/road/mobile/M0711_39_56_0_5_1.html")
data = BS(site.content, "html.parser")

print(data.title)
print(data.title.text)

elem1 = data.find_all('div')
elem2 = data.find_all('br')

elem3 = data.select('body > div:nth-of-type(4)')