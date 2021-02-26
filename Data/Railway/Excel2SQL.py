import openpyxl
import pymysql
import glob

# 說明
# 1.在不同資料庫，記得修改自己的帳密(變數db)           重要!!! (Line13)
# 2.改(Line30)路徑
# 3.執行一次即成功匯入整個excel檔案至SQL

print ("start")

# (主機名稱,帳號,密碼,資料庫名稱)
db=pymysql.connect(host="localhost",user="root",password="Dieark20000115",database="railway")
cursor=db.cursor()
# 選擇資料表
sql_select="SELECT date FROM `豐原(順行)` ORDER BY date DESC ,time DESC LIMIT 0,1;" 
cursor.execute(sql_select)
data=cursor.fetchone()
lastData=str(data[0][:4])+str(data[0][5:7])+str(data[0][-2:])
print(lastData)
i=1
k=0
while i==1:
    for filename in glob.glob(r'D:\Dieark\pythons\flask1\Collage-Project\Data\Railway\*.xlsx'): #需要修改路徑名稱
        if (filename[-13:-5]==lastData): # 比對excel名稱跟資料庫資料
            k=1
            continue
        if k==1:
            time=filename[-13:-9]+"/"+filename[-9:-7]+"/"+filename[-7:-5] #丟到資料庫的'time'
            print(time)
            wb = openpyxl.load_workbook(filename)
            for num in range(100): # 100 > 42站
                wb.active = num
                ws = wb.active
                # 取出資料表名稱
                strrr=str(ws)[12:-2] # <Worksheet "彰化(順行)">
                arr=["","","","","","",""]
                if strrr=="Sheet":
                    break
                print(strrr)
                for row in ws:
                    n=0
                    for cell in row:
                        #空指令
                        pass
                        # print(cell.value) #可印出來，檢查資料
                        arr[n]=cell.value
                        n=n+1
                    # SQL指令字串
                    sql_insert="INSERT INTO `"+strrr+"` (id,date,time,num,destination,ontime)\
                    VALUES ('%s','%s','%s','%s','%s','%s');" % (arr[0],time,arr[2],arr[1],arr[3],arr[5])
                    cursor.execute(sql_insert)
                    db.commit()
                print("done")
    else:
        i=0
print("success")