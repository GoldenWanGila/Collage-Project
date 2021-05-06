import pymysql
import pandas as pd
from pandas import DataFrame
import time

# 預設輸入
default_account = "root"
default_pw = "Dieark20000115"
default_db = "railway"

host = "localhost"
user = input("帳號(目前預設:%s):" % default_account) or default_account
pw = input("密碼(目前預設:%s):" % default_pw) or default_pw
database = input("資料庫(目前預設:%s):" % default_db) or default_db
print("")

db = pymysql.connect(host=host,user=user,password=pw,database=database)
cursor = db.cursor()

# function
def all_task():
    print("")
    print("======所有指令======")
    print('1:列出所有資料"表"')
    print("2:列出指定資料表的內容")
    print("3:列出指定車次")
    print("4:列出指定資料的上下n筆資料")
    print("9:重新連接其它資料庫")
    print("0:離開")
    print("====================")
    print("")

def easy_sql(sql):
    cursor.execute(sql)
    data = cursor.fetchall()
    new_data=[]
    for n in range(len(data)):
        new_data.append(data[n][0])
    return new_data

def result(sql, arr, data):
    cursor.execute(sql)
    if data:
        pass
    else:
        data = cursor.fetchall()

    new_data = {}
    for i in range(len(data[0])):
        exec('n%s = []' %(i))
        for k in range(len(data)):
            exec('n%s.append(data[%s][%s])' %(i, k, i))
        exec('new_data["%s"] = n%s' %(arr[i],i))
    pd.set_option('display.unicode.east_asian_width', True)
    pd.set_option('display.unicode.ambiguous_as_wide', True)
    pd_data = pd.DataFrame(new_data)
    if input("呈現出來?(0:N,1:Y):") in "1Yy":
        print("")
        print(pd_data)
        print("")
    if input("儲存?(0:N,1:Y):") in "1Yy":
        print("")
        fn = input("輸入檔名:")
        print("儲存成功")
        pd_data.to_json(r'./\%s.json' %fn)
        print("")

def task1():
    sql = "SHOW TABLES"
    arr=[str(database)]
    data = None
    result(sql, arr, data)
def task2():
    table_name = ''
    sql = "SHOW TABLES"
    arr = easy_sql(sql)
    data = None
    while len(table_name)<1:
        print("-"*100)
        print("可輸入:", *arr)
        print("-"*100)
        table_name = input("輸入想查找的資料表名稱:")
    sql = "SHOW COLUMNS FROM `%s`" % table_name
    arr = easy_sql(sql)
    print("-"*100)
    print("可輸入:", *arr)
    print("-"*100)
    col_name = input("輸入想查找的欄位名稱(ex:Precp)(大小寫需正確)(未填入視為'所有'):") or "*"
    if col_name != "*":
        arr=[]
        arr.append(col_name)
    sql = "SELECT %s FROM `%s`" % (col_name, table_name)
    result(sql, arr, data)
def task3():
    train_num = int(input("輸入想查找的車次(ex:118):"))
    sql = "SHOW TABLES"
    arr = easy_sql(sql)
    data=[]
    for n in arr:
        sql = "SELECT %s FROM `%s` WHERE num = '%d'" % ("*", n, train_num)
        cursor.execute(sql)
        data_old = cursor.fetchall()
        data.extend(data_old)
    arr=["", "date", "time", "num", "dest", "delay", "type"]
    result(sql, arr, data)
def task4():
    table_name = ''
    sql = "SHOW TABLES"
    arr = easy_sql(sql)
    data = None
    while len(table_name)<1:
        print("-"*100)
        print("可輸入:", *arr)
        print("-"*100)
        table_name = input("指定站名:")
    train_num = int(input("輸入想查找的車次(ex:118):"))
    date = input("指定日期:")
    n = int(input("指定n筆資料:")) or 2
    sql = "SELECT %s FROM `%s` WHERE num = '%d' AND date = '%s'" % ("id", table_name, train_num, date)
    cursor.execute(sql)
    id = cursor.fetchone()
    id = int(id[0]) - n -1
    sql = "SELECT %s FROM `%s` WHERE date = '%s' LIMIT %d, %d" % ("*", table_name, date, id, 2*n+1)
    arr=["id", "date", "time", "num", "dest", "delay", "type"]
    result(sql, arr, data)
def task9():
    user = input("帳號(目前預設:%s):" % default_account) or default_account
    pw = input("密碼(目前預設:%s):" % default_pw) or default_pw
    database = input("資料庫(目前預設:%s):" % default_db) or default_db
    print("")
    global db, cursor
    db = pymysql.connect(host=host,user=user,password=pw,database=database)
    cursor = db.cursor()



while 1:
    all_task()
    task = input("指令:") or '0'
    try:
        exec("task%s()" %task)
    except:
        if task == '0':
            print("")
            print("掰掰")
            print("")
            break
        print("")
        print("指令錯誤或程式碼有誤")
        time.sleep(0.5)
        continue