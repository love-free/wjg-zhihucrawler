
import pymysql.cursors
import time

# 数据库链接信息,填入自己的数据库信息
conn = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='employee',
    charset='utf8'
)

cursor = conn.cursor()

cursor.execute("select * from employee_account")
res = cursor.fetchall()
for x in res:print (x)
cursor.close()
conn.close()

