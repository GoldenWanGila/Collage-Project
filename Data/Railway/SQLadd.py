import pymysql

print ("start")


# (主機名稱,帳號,密碼,資料庫名稱)
db=pymysql.connect(host="localhost",user="root",password="Dieark20000115",database="railway")
cursor=db.cursor()
sql_select="SELECT date FROM `豐原(順行)` ORDER BY date DESC ,time DESC LIMIT 0,1;" 
cursor.execute(sql_select)
data=cursor.fetchone()
lastdata=str(data[0][:4])+str(data[0][5:7])+str(data[0][-2:])
print(lastdata)
