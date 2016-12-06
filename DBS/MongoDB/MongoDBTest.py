# _*_ coding:utf-8 _*_
import pymongo

localClient = pymongo.MongoClient('localhost', 27017)  # 连接本地数据库
excelDocument = localClient["testdb"]  # 打开名字为testdb的DB(Excel)
workSheet = excelDocument["sheet_01"]  # 打开名字为sheet_01的文档(就是work sheet)
lineData = {
    "name" : "mongo",
    "age"  : 12
}
workSheet.insert_one(lineData)  # 向文档中插入一条数据
