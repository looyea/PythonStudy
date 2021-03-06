# _*_ coding:utf-8 _*_
import pymongo
import re
import sys


def getMongoDB():
    localClient = pymongo.MongoClient('localhost', 27017)  # 连接本地数据库
    excelDocument = localClient["SPIDER"]  # 打开名字为testdb的DB(Excel)
    workSheet = excelDocument["ali"]  # 打开名字为sheet_01的文档(就是work sheet)
    return workSheet

reload(sys)
sys.setdefaultencoding('utf-8')

pattern = re.compile("^蚂蚁金服*")
workSheet = getMongoDB()

datas = workSheet\
    .find({'departmentName':{'$regex':'蚂蚁金服'}},{"name":1, "requirement": 1, "description":1, "_id":0}) \
    .limit(300)

records = list()


with file("jobs.html","w+") as myFile:
    for data in datas:
        myFile.write("<p>")
        myFile.write(data["name"])
        myFile.write("</p>")
        myFile.write("<p>")
        myFile.write(data["requirement"])
        myFile.write("</p>")
        myFile.write("<p>")
        myFile.write(data["description"])
        myFile.write("</p>")
        myFile.write("<hr/>")
    myFile.flush()
    myFile.close()
