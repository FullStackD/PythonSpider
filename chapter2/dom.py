from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.read(), "html.parser")

for child in bsObj.find("table", {"id": "giftList"}).children:
    print(child)




# 邮箱正则示例
# [A-Za-z0-9\._+]+@\.(com|org|edu|net)