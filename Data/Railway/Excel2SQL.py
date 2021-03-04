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
judge=0
if len(data)!=0:
    lastData=str(arr[1][:4])+str(arr[1][5:7])+str(arr[1][-2:])
    print(lastData)
else :
    judge=1

for filename in glob.glob(r'D:\Dieark\pythons\flask1\Collage-Project\Data\Railway\*.xlsx'): #需要修改路徑名稱
    if (filename[-13:-5]==lastData): # 比對excel名稱跟資料庫資料
        judge=1
        continue
    if judge==1:
        date=filename[-13:-9]+"/"+filename[-9:-7]+"/"+filename[-7:-5] #丟到資料庫的'date'
        print(date)
        wb = openpyxl.load_workbook(filename)
        for num in range(100): # 100 > 42站
            wb.active = num
            ws = wb.active
            # 取出資料表名稱
            station=str(ws)[12:-2] # <Worksheet "彰化(順行)">
            arr=["","","","","","",""]
            if station=="Sheet":
                break
            for row in ws:
                n=0
                for cell in row:
                    #空指令
                    pass
                    # print(cell.value) #可印出來，檢查資料
                    arr[n]=cell.value
                    n=n+1
                # 處理舊格式資料(2021/01/28以前)
                if arr[6]=="":
                    pass
                    if "準點" in arr[5]:
                        arr[6]="0"
                    elif "誤點" in arr[5]:
                        i=""
                        for n in range(len(arr[5])):
                            if arr[5][n].isdigit()==True:
                                i+=arr[5][n]
                        arr[6]=i
                    arr[4]=arr[3]
                    arr[3]=arr[2]
                    j=""
                    for n in range(len(arr[1])):
                        if arr[1][n].isdigit()==True:
                            j+=arr[1][n]
                    arr[2]=j
                    k=""
                    for n in range(len(arr[1])):
                        if arr[1][n].isdigit()==True:
                            break
                        if arr[1][n].isdigit()==False:
                            k+=arr[1][n]
                    arr[1]=k
                ###

                # SQL指令字串
                sql_insert="INSERT INTO `"+station+"` (id,date,time,num,dest,delay,type)\
                VALUES ('%s','%s','%s','%s','%s','%s','%s');" % (arr[0],date,arr[3],arr[2],arr[4],arr[6],arr[1])
                # if arr[5]!=None:
                #     sql_update="UPDATE `"+station+"` SET delay='"+arr[5]+"' WHERE id='"+arr[0]+"' AND date='"+date+"';"
                cursor.execute(sql_insert)
                db.commit()
                    
            print(station+" Done")
print("success")