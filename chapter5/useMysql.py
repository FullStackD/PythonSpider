import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='scraping')

cur = conn.cursor()
cur.execute("select * from pages")
print(cur.fetchone())

cur.close()
conn.close()