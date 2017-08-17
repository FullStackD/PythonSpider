from urllib.request import urlopen
from urllib.error import HTTPError
# DOC https://docs.python.org/3/library/urllib.html#module-urllib
from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title


title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title is None:
    print("Title could not bu found")
else:
    print(title)
