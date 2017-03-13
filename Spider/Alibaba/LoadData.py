# _*_ coding:utf-8 _*_
import pymongo
import re

def getMongoDB():
    localClient = pymongo.MongoClient('localhost', 27017)  # 连接本地数据库
    excelDocument = localClient["SPIDER"]  # 打开名字为testdb的DB(Excel)
    workSheet = excelDocument["ali"]  # 打开名字为sheet_01的文档(就是work sheet)
    return workSheet

pattern = re.compile(".*蚂蚁金服.*")
workSheet = getMongoDB()

datas = workSheet\
    .find({'departmentName':pattern},{"name":1, "requirement": 1, "description":1, "_id":0}) \
    .limit(300)

records = list()

for data in datas:
    records.append(data)

# for record in records:
    # print data["name"]
    # print data["requirement"]
    # print data["description"]
    # print "----------------"

print len(records)