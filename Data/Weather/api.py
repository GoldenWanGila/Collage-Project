import pymysql
import pandas as pd
import time

default_account="root"
default_pw="Dieark20000115"
default_db="weather"
account=input("帳號:") or default_account
pw=input("密碼:") or default_pw
database=input("資料庫:") or default_db
print("")

db=pymysql.connect(host="localhost",user=account,password=pw,database=database)
cursor=db.cursor()

def all_task():
    print("======所有指令======")
    print('1:列出所有資料"表"')
    print("2:列出指定資料")
    # print("")
    # print("")
    print("0:離開")
    print("====================")
    print("")

finish=0
while finish==0:
    all_task()
    task=input("指令:") or '0'
    if task=='0':
        db.commit()
        print("掰掰")
        break
    elif task=='1':
        sql="SHOW TABLES"
    elif task=='2':
        table_name=''
        while len(table_name)<1:
            table_name=input("輸入想查找的資料表名稱(ex:2021/01/15):")
        col_name=input("輸入想查找的欄位名稱(ex:Precp)(大小寫需正確)(未填入視為'所有'):") or "*"
        sql="SELECT %s FROM `%s`" %(col_name,table_name)
        if input("更詳細判斷?(0:N,1:Y):")==('1'or'Y'or'y'):
            where=input("欄位名稱=特定值(空格隔開):").split() or (-1,-1)
            if where[0]!=-1:
                sql="SELECT %s FROM `%s` WHERE %s = '%s'" %(col_name,table_name,where[0],where[1])
    else:
        print("白癡喔，輸入錯了齁")
        continue
    
    cursor.execute(sql)
    data=cursor.fetchall()
    new_data={}
    for i in range(len(data[0])):
        exec('n'+str(i)+'=[]')
        for k in range(len(data)):
            exec('n'+str(i)+'.append(data['+str(k)+']['+str(i)+'])')
        exec('new_data["n'+str(i)+'"]=n'+str(i)+'')
    pd_data=pd.DataFrame(new_data)
    if input("呈現出來?(0:N,1:Y):")==('1'or'Y'or'y'):
        print("")
        print(pd_data)
        print("")
    sql="SELECT * FROM "