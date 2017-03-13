# _*_ coding:utf-8 _*_
import pymongo

def getMongoDB():
    localClient = pymongo.MongoClient('localhost', 27017)  # 连接本地数据库
    excelDocument = localClient["testdb"]  # 打开名字为testdb的DB(Excel)
    workSheet = excelDocument["sheet_01"]  # 打开名字为sheet_01的文档(就是work sheet)
    return workSheet

if __
lineData = {
    "name" : "mongo",
    "age"  : 12
}
workSheet = getMongoDB()
workSheet.insert_one(lineData)  # 向文档中插入一条数据
