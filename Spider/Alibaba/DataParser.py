# _*_ coding:utf-8 _*_
import json
import pymongo
import urllib2

def getMongoDB():
    localClient = pymongo.MongoClient('localhost', 27017)  # 连接本地数据库
    excelDocument = localClient["testdb"]  # 打开名字为testdb的DB(Excel)
    workSheet = excelDocument["ali"]  # 打开名字为sheet_01的文档(就是work sheet)
    return workSheet

parameters = {}
url = "https://job.alibaba.com/zhaopin/socialPositionList/doList.json?pageSize=10&location=%E5%8C%97%E4%BA%AC"
url_data = urllib2.urlopen(url).readline()
datas = json.loads(url_data)["returnValue"]["datas"]


workSheet = getMongoDB()



for data in datas:
    workSheet.insert_one(data)  # 向文档中插入一条数据


