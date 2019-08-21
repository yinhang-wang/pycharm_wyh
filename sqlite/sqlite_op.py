import sqlite3
import time
# conn = sqlite3.connect("sql_lianxi.sqlite")
# print("Open database successfully")

conn = sqlite3.connect(":memory:")
print("Open database successfully")

cursor = conn.cursor()  # 创建cursor
# 增加
cursor.execute("drop table IF EXISTS COMPANY")
cursor.execute("CREATE TABLE COMPANY (ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL, AGE INT NOT NULL, ADDRESS CHAR(50), SALARY REAL);")

cursor.execute("INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY,ID) VALUES ('Paul', 32, 'California', 20000.00 ,103);")
# cursor.execute("INSERT INTO COMPANY VALUES (2, 'Allen', 25, 'Texas', 15000.00 );")
# cursor.execute("INSERT INTO COMPANY VALUES (3, 'jack', 40, 'Sanfran', 1233.00),(4, 'Alex', 34, 'Newyork', 10000.00 );")

# statement = "INSERT INTO COMPANY VALUES(?,?,?,?,?)"
# data = [(5, "thoms", 26, "krash", 908),(6,"binder",45,"charbriage", 730.4)]
# conn.executemany(statement, data)
conn.commit()

# # 删除
# cursor.execute("delete from COMPANY where ID =13")
# # 修改
# cursor.execute("update COMPANY set ADDRESS = 'California' where ID =%d"%(3))

# # 查询
cursor.execute("SELECT * FROM COMPANY;")
# result_all = cursor.fetchall()
# print(type(result_all))
# for row in result_all:
#     print(row)
#     print(row[1])
print("*"*30)
result_one = cursor.fetchone()
print(result_one)
# result_one = result_all[0]
# print(result_one)
print("*"*30)
# result_many = cursor.fetchmany(3)
# for each_row in result_many:
#     print(each_row)


cursor.close()  # 关闭cursor
conn.commit()  # 提交事务
conn.close()
