import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

from requests import HTTPError

random.seed(datetime.datetime.now())


# 获取某个词条内的所有wiki词条链接
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))


# 获取某个词典的所有历史编辑IP
def getHistoryIPs(pageUrl):
    # 编辑历史页面URL链接格式是：
    # http://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
    pageUrl = pageUrl.replace("/wiki/", "")
    historyUrl = "http://en.wikipedia.org/w/index.php?title=" + pageUrl + "&action=history"
    print("history url is: " + historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    # 找出class属性是"mw-anonuserlink"的链接
    # 它们用IP地址代替用户名
    ipAddresses = bsObj.findAll("a", {"class": "mw-anonuserlink"})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList


def getCountry(ipAddress):
    try:
        response = urlopen("http://freegeoip.net/json/" + ipAddress).read().decode('utf-8')
    except HTTPError:
        return None
    responseJson = json.loads(response)
    return responseJson.get("country_code")


links = getLinks("/wiki/Python_(programming_language)")
print(len(links))
number = 0
while (len(links) > 0) and (number < 10000):
    for link in links:
        number += 1
        print("-------------------")
        historyIPs = getHistoryIPs(link.attrs["href"])
        for historyIP in historyIPs:
            # print(historyIP)
            country = getCountry(historyIP)
            if country is not None:
                print(historyIP + " is from " + country)

    newLink = links[random.randint(0, len(links) - 1)].attrs["href"]
    links = getLinks(newLink)


# TODO
# 爬取1W个词条
# 使用Dic 记录国家和数量
# 英文对应到中文国家