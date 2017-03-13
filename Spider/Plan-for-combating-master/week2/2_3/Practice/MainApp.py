# _*_ coding:utf-8 _*_
'''
因为跟原来的58网站有很大变动
所以我们这里使用前几天的小猪短租的链接进行爬取.

链接中我去掉了jsonp回调的内容
http://wirelesspub.xiaozhu.com/app/xzfk/html5/500/search/result?cityId=12&offset=20&length=5

'''
from multiprocessing import Pool
from bs4 import BeautifulSoup
import requests
import pymongo


def getData(url):
    try:
        web_data = requests.get(url)
        soup = BeautifulSoup(web_data.text,'lxml')
        resultText = soup.p.text
        resultText = resultText.replace("true", "True")
        resultText = resultText.replace("false", "False")
        resultDic = eval(resultText)
        items = resultDic["content"]["item"]
        for item in items:
            sheet.insert_one(item)
            # print(item["luTitle"].strip() + " -> " + item["luLeaseType"].strip() + " -> " + item["displayAddr"].strip() + " : " + str(item["luPrice"]))
        return 1
    except:
        return 0

client = pymongo.MongoClient("localhost", 27017)
document = client["xiaozhu"]
sheet = document["bj_duanzu"]

urls = ["http://wirelesspub.xiaozhu.com/app/xzfk/html5/500/search/result?cityId=12&offset={}&length=10".format(str(i) ) for i in range(0,500, 10) ]

for url in urls:
    ret = getData(url)
    if ret == 0 :
        break
    else:
        continue

# getData("http://wirelesspub.xiaozhu.com/app/xzfk/html5/500/search/result?cityId=12&offset=0&length=1")

# 创建进程池子
# pool = Pool(processes*6) # 后面的内容是指用多少个进程来完成, 这里是6个进程
# pool = Pool()
'''
这里是个map函数, 就是吧后面chennal.split()之后的list中的每一项, 放到newFunct中作为参数运行
Pool中会根据你开始给的内容, 自动分配进程进行处理

不过windows下运行还有个问题, 就是会报错啊

'''
# pool.map(newFunct, chennal.split())
# pool.map(getData, urls.split())



