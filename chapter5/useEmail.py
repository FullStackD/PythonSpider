import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time


def sendMail(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = ''
    msg['To'] = ''
    msg['']
    s = smtplib.SMTP('smtp.sina.com')
    s.login('', '')
    s.send_message(msg)
    s.quit()


bsObj = BeautifulSoup(urlopen("https://isitchristmas.com/"), "html.parser")

while bsObj.find("a", {"id": "answer"}).attrs['title'] == "唔係":
    print("It is not Christmas yet.")
    time.sleep(3600)
    bsObj = BeautifulSoup(urlopen("https://isitchristmas.com/"))
sendMail("It's Christmas!", "According to http://itischristmas.com, it is Christmas!")
