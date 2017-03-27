# _*_ coding:utf-8 _*_

import pymongo
import sys


def getMongoDB():
    localClient = pymongo.MongoClient('localhost', 27017)  # 连接本地数据库
    excelDocument = localClient["SPIDER"]  # 打开名字为testdb的DB(Excel)
    workSheet = excelDocument["mooc"]  # 打开名字为sheet_01的文档(就是work sheet)
    return workSheet

reload(sys)
sys.setdefaultencoding( "utf-8" )

workSheet = getMongoDB()


datas = workSheet.find().sort('name', pymongo.ASCENDING)

dataSet = set()

for data in datas:
    dataSet.add(data["name"])


with open("D:\\name.txt","w") as myfile:
    for data in dataSet:
        myfile.write(data + "\n")
    myfile.flush()
    myfile.close()