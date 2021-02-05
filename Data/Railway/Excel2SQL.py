import openpyxl
import pymysql

# 說明
# 1.修改excel名稱(變數fn)，並確定前者有在資料夾中
# 2.修改日期字串(變數time)，前者為抓取日期
# 3.在不同資料庫，記得修改自己的帳密(變數db)
# 4.執行一次即成功匯入整個excel檔案至SQL
# 5.重複上面動作

print ("start")

# (主機名稱,帳號,密碼,資料庫名稱)
db=pymysql.connect(host="localhost",user="root",password="lesson116",database="railway")
cursor=db.cursor()

# 修改陣列中數字以符合xlsx檔名
for date in ['08','09',10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]:
    # excel的名稱，前者檔案須放在與此py檔同一層資料夾
    fn = 'Data collector 202101'+str(date)+'.xlsx'
    wb = openpyxl.load_workbook(fn)

    # 日期必須修改，為excel資料的抓取日期
    time="01/"+str(date)

    # 14個資料表(7站*(順、逆))
    for num in range(14):
        wb.active = num
        ws = wb.active
        strr=str(ws)
        # 取出資料表名稱
        strrr=strr[12:-2]
        arr=["","","","","","",""]

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
    

print("success")
