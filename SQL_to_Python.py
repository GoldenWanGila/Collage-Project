import pymysql

host = 'localhost'
user = ''
passwd = ''
database = ''

eng = pymysql.connect(host=host, user=user, password=passwd, db=database, charset='utf8')

