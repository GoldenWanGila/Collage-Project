import pymysql

db=pymysql.connect(host="localhost",user="root",password="lesson116",database="railway")
cursor=db.cursor()

sql_create="CREATE TABLE `railway`.`彰化(逆行)` ( `id` VARCHAR(3) NOT NULL , `date` VARCHAR(10) NOT NULL , `time` VARCHAR(10) NOT NULL , `num` VARCHAR(100) NOT NULL , `destination` VARCHAR(5) NOT NULL , `ontime` VARCHAR(10) NOT NULL ) ENGINE = MyISAM;"
cursor.execute(sql_create)
db.commit()
print("success")