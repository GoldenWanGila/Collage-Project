import pymysql
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# 連接資料庫
db=pymysql.connect(host="localhost",user="root",password="Dieark20000115",database="railway")
cursor=db.cursor()

stationName=["豐原(順行)","豐原(逆行)","太原(順行)","太原(逆行)","臺中(順行)","臺中(逆行)","潭子(順行)","潭子(逆行)","新烏日(順行)","新烏日(逆行)","彰化(順行)","彰化(逆行)","員林(順行)","員林(逆行)","基隆(順行)","基隆(逆行)","汐止(順行)","汐止(逆行)","臺北(順行)","臺北(逆行)","板橋(順行)","板橋(逆行)","桃園(順行)","桃園(逆行)","中壢(順行)","中壢(逆行)","新竹(順行)","新竹(逆行)","竹南(順行)","竹南(逆行)","苗栗(順行)","苗栗(逆行)","斗六(順行)","斗六(逆行)","嘉義(順行)","嘉義(逆行)","臺南(順行)","臺南(逆行)","新左營(順行)","新左營(逆行)","高雄(順行)","高雄(逆行)"]
typeName=["自強","太魯閣","普悠瑪","莒光","觀光列車","商務列車","復興","區間","區間快"]
# sql_select="SELECT time FROM `臺中(順行)` WHERE date='2021/01/15';"
# sql_select="SELECT time FROM `臺中(順行)`;"
# cursor.execute(sql_select)
# data=cursor.fetchall()

data=[]
for sn in stationName:
    sql_select="SELECT time FROM `"+sn+"`;"
    cursor.execute(sql_select)
    data1=cursor.fetchall()
    for n in data1:
        data.append(n)
print("data",len(data))
db.commit()

times=[]
for n in range(len(data)):
    times.append(data[n][0])
times.sort()
x_count=[]
temp='05'
count=0
for n in times:
    m=n[:2]
    if temp!=m:
        x_count.append(count)
        temp=m
        count=1
    else:
        count+=1
else:
    x_count.append(count)

# print(times)
print(x_count)
print("success")

x=[]
for n in range(24):
    x.append(n)
x.append(24)
y=[0]
y.extend(x_count)
y.append(0)

# slope, intercept, r, p, std_err = stats.linregress(x, y)

# def myfunc(x):
#   return slope * x + intercept

# mymodel = list(map(myfunc, x))
print(len(x),len(y))
print(y)
plt.scatter(x, y)
# plt.plot([1,24], [800,800])
plt.plot(y, ls='dashed')
plt.xlabel('time session')
plt.ylabel('total count')
plt.xlim([0,24])
# plt.ylim([0,10])
plt.xticks(x)
plt.show()