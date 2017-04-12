# _*_ coding:utf-8 _*_

import json
import pymongo
import urllib2
import time
import requests
from bs4 import BeautifulSoup


def getMongoDB():
    localClient = pymongo.MongoClient('localhost', 27017)  # 连接本地数据库
    excelDocument = localClient["SPIDER"]  # 打开名字为testdb的DB(Excel)
    workSheet = excelDocument["educsdn"]  # 打开名字为sheet_01的文档(就是work sheet)
    return workSheet

headers = {
    "Cookie" : "uuid_tt_dd=-815709850406859162_20170111; __utma=17226283.1332556033.1489400236.1489400236.1489400236.1; __utmz=17226283.1489400236.1.1.utmcsr=sogou|utmccn=(organic)|utmcmd=organic|utmctr=python%20mongodb%20find; _ga=GA1.2.1332556033.1489400236; UN=looyea; UE=\"looyea@yeah.net\"; BT=1489469064832; _JQCMT_ifcookie=1; _JQCMT_browser=e27d8ae63addfa80068f4c41ec5a238d; PHPSESSID=pp54bpjbvq6laneg5g5masvjb5; dc_tos=oo83k0; dc_session_id=1491876677413; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1491038483,1491038500,1491039299,1491876678; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1491876865",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36"
}

urls = ["http://www.imooc.com/course/ajaxcourserecom?cid={}".format(str(i) ) for i in range(5, 1000)]

workSheet = getMongoDB()

for url in urls:
    try:
        time.sleep(1)
        web_data = requests.get(url, headers)
        Soup = BeautifulSoup(web_data.text, 'lxml')

    except Exception as e:
        print("Cant find url " + url)
        continue

