import pymysql
import matplotlib.pyplot as plt
import numpy as np
import time
from scipy import stats


# # 降雨量-氣溫關係 start
# # 連接資料庫(記得修改參數)
# db=pymysql.connect(host="localhost",user="root",password="Dieark20000115",database="weather")
# cursor=db.cursor()
# sql_select="SHOW TABLES"
# cursor.execute(sql_select)
# data=cursor.fetchall()
# data=data[9:] # 排除掉12/15以前的資料
# x=[]
# y=[]
# for n in data:
#     table_name=n[0]
#     sql_select="SELECT Temperature FROM `"+table_name+"`;"
#     cursor.execute(sql_select)
#     data1=cursor.fetchall()
#     print(data1)
#     for m in data1:
#         x.append(m[0])
#     sql_select="SELECT Precp FROM `"+table_name+"`;"
#     cursor.execute(sql_select)
#     data2=cursor.fetchall()
#     for l in data2:
#         y.append(l[0])
# db.commit()

# for n in range(len(y)):
#     if y[n]=='None':
#         y[n]='0'
#     if y[n]=='T':
#         y[n]='0.05'
# for n in range(len(x)):
#     x[n]=float(x[n])
#     y[n]=float(y[n])
# x.sort()
# y.sort()

# print(len(x),len(y))
# plt.scatter(x, y)
# plt.plot(y, ls='dashed')
# plt.xlabel('Temperature')
# plt.ylabel('RainFall')
# plt.xlim([10,40])
# plt.ylim([0,4])
# plt.xticks([10,20,30])
# plt.show()

# # 降雨量-氣溫關係 end

# =====================================================================================================

# # 發車時間次數-時間關係 start
# # 連接資料庫(記得修改參數)
# db=pymysql.connect(host="localhost",user="root",password="Dieark20000115",database="railway")
# cursor=db.cursor()
# stationName=["豐原(順行)","豐原(逆行)","太原(順行)","太原(逆行)","臺中(順行)","臺中(逆行)","潭子(順行)","潭子(逆行)","新烏日(順行)","新烏日(逆行)","彰化(順行)","彰化(逆行)","員林(順行)","員林(逆行)","基隆(順行)","基隆(逆行)","汐止(順行)","汐止(逆行)","臺北(順行)","臺北(逆行)","板橋(順行)","板橋(逆行)","桃園(順行)","桃園(逆行)","中壢(順行)","中壢(逆行)","新竹(順行)","新竹(逆行)","竹南(順行)","竹南(逆行)","苗栗(順行)","苗栗(逆行)","斗六(順行)","斗六(逆行)","嘉義(順行)","嘉義(逆行)","臺南(順行)","臺南(逆行)","新左營(順行)","新左營(逆行)","高雄(順行)","高雄(逆行)"]
# typeName=["自強","太魯閣","普悠瑪","莒光","觀光列車","商務列車","復興","區間","區間快"]

# data=[]
# for sn in stationName:
#     sql_select="SELECT time FROM `"+sn+"`;"
#     cursor.execute(sql_select)
#     data1=cursor.fetchall()
#     for n in data1:
#         data.append(n)
# print("data",len(data))
# db.commit()

# times=[]
# for n in range(len(data)):
#     times.append(data[n][0])
# times.sort()
# x_count=[]
# temp='05'
# count=0
# for n in times:
#     m=n[:2]
#     if temp!=m:
#         x_count.append(count)
#         temp=m
#         count=1
#     else:
#         count+=1
# else:
#     x_count.append(count)

# # print(times)
# print(x_count)
# print("success")

# x=[]
# for n in range(24):
#     x.append(n)
# x.append(24)
# y=[]
# y.extend(x_count)
# y.append(0)


# # slope, intercept, r, p, std_err = stats.linregress(x, y)

# # def myfunc(x):
# #   return slope * x + intercept

# # mymodel = list(map(myfunc, x))
# print(len(x),len(y))
# plt.scatter(x, y)
# plt.plot(y, ls='dashed')
# plt.xlabel('time session')
# plt.ylabel('total count')
# plt.xlim([0,24])
# plt.xticks(x)
# plt.show()
# # 發車時間次數-時間關係 end

# ======================================================================================


# 降雨量-誤點關係 start

sql_select="SHOW TABLES"

x=[]
y=[]
    
db_w=pymysql.connect(host="localhost",user="root",password="Dieark20000115",database="weather")
cursor_w=db_w.cursor()
cursor_w.execute(sql_select)
data_w=cursor_w.fetchall()

db_r=pymysql.connect(host="localhost",user="root",password="Dieark20000115",database="railway")
cursor_r=db_r.cursor()

for n in range(len(data_w)):
    # print(data_w[n][0])
    sql_s_time="SELECT ObsTime FROM `"+data_w[n][0]+"`;"
    cursor_w.execute(sql_s_time)
    data_s_time=cursor_w.fetchall()
    for m in range(len(data_s_time)):

        sql_s_rain="SELECT Precp FROM `"+data_w[n][0]+"` WHERE ObsTime='"+data_s_time[m][0]+"'"
        cursor_w.execute(sql_s_rain)
        data_s_rain=cursor_w.fetchall()
        for i in data_s_rain:
            x.append(i[0])

        station_name="臺中(順行)"
        sql_s_delay="SELECT delay FROM `"+station_name+"` WHERE date='"+data_w[n][0]+"' AND time LIKE '"+data_s_time[m][0][:2]+":%'"
        cursor_r.execute(sql_s_delay)
        data_s_delay=cursor_r.fetchall()
        
        avg=0
        count=0
        for l in data_s_delay:
            if len(l[0])>0:
                avg+=int(l[0])
                count+=1
        else:
            if count>0:
                avg=avg/count
                y.append('%.2f' %avg)
            else:
                y.append(0)
        # print(data_s_time[m][0],'%.2f' %avg)


db_w.commit()
db_r.commit()

for n in range(len(x)):
    if x[n]=='None':
        x[n]='0'
    if x[n]=='T':
        x[n]='0.05'

for n in range(len(x)):
    x[n]=float(x[n])
    y[n]=float(y[n])

print(len(x),len(y))
plt.scatter(x, y)
plt.plot(y, ls='dashed')
plt.xlabel('RainFall')
plt.ylabel('delay')
plt.xlim([-1,4])
plt.ylim([0,20])
plt.xticks([0,0.5,1,1.5,2,2.5,3,3.5,4])
plt.show()

# 降雨量-誤點關係 end