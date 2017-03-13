# _*_ coding:utf-8 _*_
'''
本次爬取的是阿里工作网站的网页
这个网页内容很有意思, 首先每个页面的生成完全是预先做好的.
利用浏览器存储在用户本地的json数据, 直接根据数据生成界面.
其实当用户查找工作列表的时候, 内部的数据就已经完全生成了.
则时候,当用户访问工作内容详细页面的时候, 就会直接呈现.

我们这里爬取了10条数据, 并且放入到了MongoDB中作为数据存储.
'''
import json
import pymongo
import urllib2
def getMongoDB():
    localClient = pymongo.MongoClient('localhost', 27017)  # 连接本地数据库
    excelDocument = localClient["SPIDER"]  # 打开名字为testdb的DB(Excel)
    workSheet = excelDocument["ali"]  # 打开名字为sheet_01的文档(就是work sheet)
    return workSheet





def processData(datas):
    for data in datas:
        print data
        print data["name"]
        workSheet.insert_one(data)  # 向文档中插入一条数据

workSheet = getMongoDB()
pageNumbers = [i for i in range (1,21)]

url_base = "https://job.alibaba.com/zhaopin/socialPositionList/doList.json?pageSize=50&location=%E5%8C%97%E4%BA%AC&pageIndex="

datas = []
for no in pageNumbers:
    url = url_base + str(no)
    # url = "https://job.alibaba.com/zhaopin/socialPositionList/doList.json?pageSize=1&location=%E5%8C%97%E4%BA%AC&pageIndex=1"
    print url
    url_data = urllib2.urlopen(url).readline()
    datas = json.loads(url_data)["returnValue"]["datas"]
    print len(datas)
    print datas
    processData(datas)



