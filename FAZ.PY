import pymysql
import pandas as pd

mydb = pymysql.connect(host="127.0.0.1", port=3306,
                       user="root", passwd="", database="quiz game")
c = mydb.cursor()

c.execute(' SELECT `date_time` FROM `score` WHERE user_name=%s',('dk'))
res4 = c.fetchall()

dt=[]

for i in res4:
    l = list(i)
    dt.append(pd.to_datetime(l[0]))
print(dt,'xd')
print(dt[0])

for i in dt:
    print(i)
