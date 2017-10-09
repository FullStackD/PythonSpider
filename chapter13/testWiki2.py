import random
import urllib
from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
import unittest


class TestWikipedia(unittest.TestCase):
    def test_PageProperties(self):
        url = "http://en.wikipedia.org/wiki/Monty_Python"
        # 测试遇到的前100个页面
        for i in range(1, 100):
            bsObj = BeautifulSoup(urlopen(url), "html.parser")
            titles = self.titleMatchesURL(bsObj, url)
            self.assertEqual(titles[0], titles[1])
            self.assertTrue(self.contentExists(bsObj))
            url = self.getNextLink(url)
        print("Done!")

    # 检测标题和URL中的title是否匹配
    def titleMatchesURL(self, bsObj, url):
        pageTitle = bsObj.find("h1").get_text()
        urlTitle = url[(url.index("/wiki/") + 6):]
        urlTitle = urlTitle.replace("_", " ")
        urlTitle = urllib.parse.unquote(urlTitle)
        return [pageTitle.lower(), urlTitle.lower()]

    # 检测内容是否存在
    def contentExists(self, bsObj):
        content = bsObj.find("div", {"id": "mw-content-text"})
        if (content is not None):
            return True
        return False

    def getNextLink(self, url):
        html = urlopen(url)
        bsObj = BeautifulSoup(html, "html.parser")
        links = bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
        return "http://en.wikipedia.org" + links[random.randint(0, len(links) - 1)].attrs['href']


if __name__ == '__main__':
    unittest.main()
