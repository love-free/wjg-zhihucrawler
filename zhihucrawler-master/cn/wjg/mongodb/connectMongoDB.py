#encoding=utf-8
from pymongo import *

#获取客户端，建立连接
client=MongoClient("localhost",27017)

#获取数据库
db=client.pythonlib

#获取集合
stu=db.pythondata

#增加
#stu.insert_one({'name':'li','age':23})

#修改
# stu.update_one({'name':'dd'},{'$set':{'name':'abc'}})

#删除
# stu.delete_one({'name':'li'})

#查询
cursor=stu.find({'age':{'$gte':20}}).sort('_id',-1 )
for s in cursor:
    print(s['name']+"\t"+str(s['age']))

#打印集合数据的总个数
print(stu.count())