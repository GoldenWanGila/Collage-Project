import pymysql

db=pymysql.connect(host="localhost",user="root",password="Dieark20000115",database="railway")
cursor=db.cursor()

stationName=["豐原(順行)","豐原(逆行)","太原(順行)","太原(逆行)","臺中(順行)","臺中(逆行)","潭子(順行)","潭子(逆行)","新烏日(順行)","新烏日(逆行)","彰化(順行)","彰化(逆行)","員林(順行)","員林(逆行)","基隆(順行)","基隆(逆行)","汐止(順行)","汐止(逆行)","臺北(順行)","臺北(逆行)","板橋(順行)","板橋(逆行)","桃園(順行)","桃園(逆行)","中壢(順行)","中壢(逆行)","新竹(順行)","新竹(逆行)","竹南(順行)","竹南(逆行)","苗栗(順行)","苗栗(逆行)","斗六(順行)","斗六(逆行)","嘉義(順行)","嘉義(逆行)","臺南(順行)","臺南(逆行)","新左營(順行)","新左營(逆行)","高雄(順行)","高雄(逆行)"]
typeName=["自強","太魯閣","普悠瑪","莒光","觀光列車","商務列車","復興","區間","區間快"]
for station in stationName:
    pass
    ### 在資料庫所有資料表新增新的欄位(2變數:名稱、字串長度) ###
    # sql_add_col="ALTER TABLE `"+station+"` ADD type varchar(10);"
    # cursor.execute(sql_add_col)
    # db.commit()

    ### 在資料庫新增新的資料表 ###
    # sql_create_table="CREATE TABLE `railway`.`"+station+"` ( `id` VARCHAR(3) NOT NULL , `date` VARCHAR(10) NOT NULL , `time` VARCHAR(10) NOT NULL , `num` VARCHAR(100) NOT NULL , `destination` VARCHAR(5) NOT NULL , `ontime` VARCHAR(10) NOT NULL ) ENGINE = MyISAM;"
    # cursor.execute(sql_create_table)
    # db.commit()

    ### 在資料庫所有資料表更改某欄位名稱(or其他參數設定) ###
    # sql_change_col_name="ALTER TABLE `"+station+"` CHANGE `destination` `dest` VARCHAR(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL;"
    # cursor.execute(sql_change_col_name)
    # db.commit()

    ### 在資料庫所有資料表更新num欄位內容 ###
    # sql_select="SELECT num FROM `"+station+"`"
    # cursor.execute(sql_select)
    # data=cursor.fetchall()
    # i=""
    # for n in data:
    #     for k in range(len(n[0])):
    #         if n[0][k].isdigit()==True:
    #             i+=n[0][k]
    #     if len(i)>0:
    #         sql_alter_num_col="UPDATE `"+station+"` SET num='"+i+"' WHERE num='"+n[0]+"';"
    #         cursor.execute(sql_alter_num_col)
    #         db.commit()
    #         print(i)
    #     i=""
    
    ### 在資料庫所有資料表更新type欄位內容 ###
    # for typeN in typeName:
    #     sql_alter_type_col="UPDATE `"+station+"` SET type='"+typeN+"' WHERE num LIKE '%"+typeN+"%';"
    #     cursor.execute(sql_alter_type_col)
    #     db.commit()

    ### 在資料庫所有資料表更新delay欄位內容 ###
    # sql_select_delay_col="SELECT * FROM `"+station+"` WHERE delay NOT LIKE '誤點%' AND delay NOT LIKE '準點'"
    # sql_select_delay_col="SELECT * FROM `"+station+"` WHERE delay LIKE '準點'"
    # sql_select_delay_col="SELECT * FROM `"+station+"` WHERE delay LIKE '誤點%'"
    # sql_alter_delay_col="UPDATE `"+station+"` SET delay='0' WHERE delay LIKE '準點';"
    # cursor.execute(sql_select_delay_col)
    # db.commit()
    # data=cursor.fetchall()
    # for n in data:
    #     i=""
    #     for k in range(len(n[5])):
    #         if n[5][k].isdigit()==True:
    #             i+=n[5][k]
    #     if len(i)>0:
    #         sql_alter_delay_col="UPDATE `"+station+"` SET delay='"+i+"' WHERE delay='"+n[5]+"';"
    #         cursor.execute(sql_alter_delay_col)
    #         db.commit()

    ### 在資料庫所有資料表delete某條件列 ###
    # sql_delete="DELETE FROM `"+station+"` WHERE date='2021/01/29';"
    sql_delete="SELECT * FROM `"+station+"` WHERE date='2020/12/15';"
    cursor.execute(sql_delete)
    data=cursor.fetchall()
    if len(data)==0:
        print("nothing")
    db.commit()
    print(station+" Done")
print("success")