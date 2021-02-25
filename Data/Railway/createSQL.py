import pymysql

db=pymysql.connect(host="localhost",user="root",password="Dieark20000115",database="railway")
cursor=db.cursor()

listname=[
# "豐原(順行)",
# "豐原(逆行)",
# "太原(順行)",
# "太原(逆行)",
# "臺中(順行)",
# "臺中(逆行)",
# "潭子(順行)",
# "潭子(逆行)",
# "新烏日(順行)",
# "新烏日(逆行)",
# "彰化(順行)",
# "彰化(逆行)",
# "員林(順行)",
# "員林(逆行)",
"基隆(順行)",
"基隆(逆行)",
"汐止(順行)",
"汐止(逆行)",
"臺北(順行)",
"臺北(逆行)",
"板橋(順行)",
"板橋(逆行)",
"桃園(順行)",
"桃園(逆行)",
"中壢(順行)",
"中壢(逆行)",
"新竹(順行)",
"新竹(逆行)",
"竹南(順行)",
"竹南(逆行)",
"苗栗(順行)",
"苗栗(逆行)",
"斗六(順行)",
"斗六(逆行)",
"嘉義(順行)",
"嘉義(逆行)",
"臺南(順行)",
"臺南(逆行)",
"新左營(順行)",
"新左營(逆行)",
"高雄(順行)",
"高雄(逆行)"]
for listn in listname:
    sql_create="CREATE TABLE `railway`.`"+listn+"` ( `id` VARCHAR(3) NOT NULL , `date` VARCHAR(10) NOT NULL , `time` VARCHAR(10) NOT NULL , `num` VARCHAR(100) NOT NULL , `destination` VARCHAR(5) NOT NULL , `ontime` VARCHAR(10) NOT NULL ) ENGINE = MyISAM;"
    cursor.execute(sql_create)
    db.commit()
print("success")