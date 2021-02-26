import pymysql

print ("start")
list1=["豐原(順行)","豐原(逆行)","太原(順行)","太原(逆行)","臺中(順行)","臺中(逆行)","潭子(順行)","潭子(逆行)","新烏日(順行)","新烏日(逆行)","彰化(順行)","彰化(逆行)","員林(順行)","員林(逆行)"]


# (主機名稱,帳號,密碼,資料庫名稱)
for listname in list1:
    db=pymysql.connect(host="localhost",user="root",password="Dieark20000115",database="railway")
    cursor=db.cursor()
    sql_select="SELECT date FROM `"+listname+"`;" 
    cursor.execute(sql_select)
    j=0
    while j==0:
        data = cursor.fetchone()   #fetchall返回查詢的全部資料， 返回元組型別資料
        if data!=None:
            if (str(data[0])[:2]=='01'):
                date=str(data[0])[-2:]
                print(data)
                sql_update="UPDATE `"+listname+"` SET date='2021/01/"+date+"' WHERE date='01/"+date+"'" 
                cursor.execute(sql_update)
        if data==None:
            j=1
        else:
            lastData=str(data[0])
            lastData=lastData[:2]+lastData[-2:]
    else:
        print('lastData=',lastData)

print("done")