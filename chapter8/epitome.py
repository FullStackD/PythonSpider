from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
import operator


def isCommon(ngram):
    commonWords = ["the", "be", "and", "of", "a", "in", "to", "have", "it",
                   "i", "that", "for", "you", "he", "with", "on", "do", "say", "this",
                   "they", "is", "an", "at", "but", "we", "his", "from", "that", "not",
                   "by", "she", "or", "as", "what", "go", "their", "can", "who", "get",
                   "if", "would", "her", "all", "my", "make", "about", "know", "will",
                   "as", "up", "one", "time", "has", "been", "there", "year", "so",
                   "think", "when", "which", "them", "some", "me", "people", "take",
                   "out", "into", "just", "see", "him", "your", "come", "could", "now",
                   "than", "like", "other", "how", "then", "its", "our", "two", "more",
                   "these", "want", "way", "look", "first", "also", "new", "because",
                   "day", "more", "use", "no", "man", "find", "here", "thing", "give",
                   "many", "well"]
    for word in ngram:
        if word in commonWords:
            return True
    return False


def cleanInput(input):
    input = re.sub('\n+', " ", input).lower()  # 换行符替换为空格
    input = re.sub('\[[0-9]*\]', "", input)  # 剔除维基百科的引用标记
    input = re.sub(' +', " ", input)
    input = bytes(input, "UTF-8")
    input = input.decode("ascii", "ignore")  # 转码过程忽略异常
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)  # 去除各种符号
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput


def ngrams(input, n):
    input = cleanInput(input)
    output = {}  # 初始化字典
    for i in range(len(input) - n + 1):
        ngramTemp = " ".join(input[i:i + n])
        if ngramTemp not in output:
            output[ngramTemp] = 0
        output[ngramTemp] += 1
    return output


content = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
ngrams = ngrams(content, 2)
# operator.itemgetter(1)为获取第一个对象的值
# reverse=True为降序排列
sortedNGrams = sorted(ngrams.items(), key=operator.itemgetter(1), reverse=True)
print(sortedNGrams)
