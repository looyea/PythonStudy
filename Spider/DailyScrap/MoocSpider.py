# _*_ coding:utf-8 _*_

import json
import pymongo
import urllib2
import time


def getMongoDB():
    localClient = pymongo.MongoClient('localhost', 27017)  # 连接本地数据库
    excelDocument = localClient["SPIDER"]  # 打开名字为testdb的DB(Excel)
    workSheet = excelDocument["mooc"]  # 打开名字为sheet_01的文档(就是work sheet)
    return workSheet

headers = {
    "Cookie" : "PHPSESSID=44vohgk23gbb0dfan70uud7tn3; imooc_uuid=0a577bdb-0806-413b-8176-fbd819d3d211; imooc_isnew=1; imooc_isnew_ct=1490601687; channel=491b6f5ab9637e8f6dffbbdd8806db9b_phpkecheng; Hm_lvt_f0cfcccd7b1393990c78efdeebff3968=1490601689; Hm_lpvt_f0cfcccd7b1393990c78efdeebff3968=1490603013; IMCDNS=0; cvde=58d8c6d7e0be5-257",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36"
}

urls = ["http://www.imooc.com/course/ajaxcourserecom?cid={}".format(str(i) ) for i in range(5, 1000)]

workSheet = getMongoDB()

for url in urls:
    try:
        time.sleep(1)
        url_data = urllib2.urlopen(url).readline()
        datas = json.loads(url_data)["data"]
        if ( len(datas) > 0 ):
            for data in datas:
                workSheet.insert_one(data)
                print(data["name"])
        print(len(datas), "条数据已经写入...")
    except Exception as e:
        print("Cant find url " + url)
        continue

