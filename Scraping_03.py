# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 18:06:13 2021

@author: mgkog
"""

import requests
from bs4 import BeautifulSoup as BS

site = requests.get("http://www.skr.mlit.go.jp/road/info/pop_data.html?codes=60%3A88%3A742%3A53%3A0%3A33&subtype=0&dettype=3")
data = BS(site.content, "html.parser")

print(data.title)
print(data.title.text)

elem1 = data.find_all('div')
elem2 = data.find_all('br')
