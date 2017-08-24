from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import csv


def getTbodys(i):
    html = urlopen("http://www.cskaoyan.com/forum/forum-84-" + str(i) + ".html")
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.findAll("tbody")


# 打开CSV文件a
csvFile = open("E:\AndroidLearning/test.csv", 'w+', newline='')
writer = csv.writer(csvFile)

pageSize = 8
start_time = time.strptime("2015-7-1 0:0", '%Y-%m-%d %H:%M')  # 最早时间
baseUrl = "http://www.cskaoyan.com/forum/"
for num in range(1, pageSize):
    for tbody in getTbodys(num):
        thTag = tbody.find("a", {"class": "s xst"})  # 链接+标题
        timeTag = tbody.find("td", {"class": "by"})  # 作者发布时间
        if thTag is not None:
            d = timeTag.find("em").get_text()
            timeTuple = time.strptime(d, '%Y-%m-%d %H:%M')
            if timeTuple > start_time:
                print(baseUrl + thTag["href"], end="\t")  # 链接
                print(thTag.get_text(), end="\t")  # 标题
                print(d)  # 时间
                writer.writerow((baseUrl + thTag["href"], thTag.get_text(), d))
