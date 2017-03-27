# _*_ coding:utf-8 _*_
import pymongo

def getMongoDB():
    localClient = pymongo.MongoClient('localhost', 27017)  # 连接本地数据库
    excelDocument = localClient["test"]  # 打开名字为testdb的DB(Excel)
    workSheet = excelDocument["test"]  # 打开名字为sheet_01的文档(就是work sheet)
    return workSheet