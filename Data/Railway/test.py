# import math
# data[0]="區間快102(彰化->雲林)"
# print(data[0])
# t=""
# i=""
# for n in range(len(data[0])):
#     if data[0][n].isdigit()==True:
#         break
#     if data[0][n].isdigit()==False:
#         t+=data[0][n]

# for n in range(len(data[0])):
#     if data[0][n].isdigit()==True:
#         i+=data[0][n]

# print(t+","+i)

# import pymysql

# db=pymysql.connect(host="localhost",user="root",password="Dieark20000115",database="railway")
# cursor=db.cursor()
# sql_alter_content="SELECT num FROM `豐原(順行)`"
# cursor.execute(sql_alter_content)
# data=cursor.fetchall()
# i=""
# for n in data:
#     for k in range(len(n[0])):
#         if n[0][k].isdigit()==True:
#             i+=n[0][k]
#     if len(i)>0:
#         # sql_alter_content="UPDATE `"+station+"` SET num='"+i+"' WHERE num='"+data[0]+"';"
#         # cursor.execute(sql_alter_content)
#         # db.commit()
#         print(i)
#     i=""

# print(data[0])
# sql_select="SELECT id FROM `豐原(順行)` WHERE num='"+data[0]+"';"
# cursor.execute(sql_select)
# data=cursor.fetchone()

# while data!=None:
#     print(data[0])
#     for n in range(len(data[0])):
#         if data[0][n].isdigit()==True:
#             i+=data[0][n]
#     if len(i)>0:
#         print(i)
#     i=""
#     data=cursor.fetchone()
# db.commit()

listt="誤點  5705 分%p"

if "570 " in listt:
    print("誤點")