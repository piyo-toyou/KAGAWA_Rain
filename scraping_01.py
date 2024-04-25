import requests
from bs4 import BeautifulSoup
response = requests.get("http://www.skr.mlit.go.jp/road/info/pop_data.html?codes=60%3A88%3A732%3A52%3A0%3A21&subtype=0&dettype=3/")
print (response.text)
html_doc = requests.get("http://www.skr.mlit.go.jp/road/info/pop_data.html?codes=60%3A88%3A732%3A52%3A0%3A21&subtype=0&dettype=3").text
soup = BeautifulSoup(html_doc, 'html.parser') # BeautifulSoupの初期化
print(soup.prettify())

# TODO1 このページのaタグをすべて抜き出してください。(HTMLの内容)
real_page_tags = soup.find_all("a")
for tag in real_page_tags:
    print(tag)

# TODO2 このページのaタグをすべて抜き出してください。(HTMLの内容)

for tag in real_page_tags:
    print(tag.string)
# TODO3 このページのaタグをすべて抜き出してください。(HTMLの内容)

for tag in real_page_tags:
    print(tag.get("href"))