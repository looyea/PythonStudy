# _*_ coding:utf-8 _*_

'''
爬取网络上的图书
关键在于这里每个图书本质上都是一张高清图片
通过爬虫可以清楚的下载下来
'''

import os
import time
from urllib import urlretrieve


book_names = {
    3184197: "大话统计学",
    2112: "大话数据挖掘"
}

page_limits = {
    3184197:  423,
    2112:  283
}

headers = {
    "Cookie" : '_gid=113698815; _gidv=a32d2dbbf1b1a7ab1dd3cfa1441e7f6e; PHPSESSID=meb17pbngh9960iicd5ud07en3; ad_time=alert_ad_time; fsource=Ydyi1s8tLrTiUbyu; kw=%E5%A4%A7%E8%AF%9D%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98; Hm_lvt_c09e990373678f912c0cbcf12c86071c=1499222686; Hm_lpvt_c09e990373678f912c0cbcf12c86071c=1499225496',
    "User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36'
}


url_pattern = "http://img.bookask.com/book/page/img/{}/{}.html"
save_path = "d:\\"

for x in book_names.keys():
    pageLimit = page_limits[x]
    bookName = book_names[x]
    print "当前处理的图书《{}》 页码{}".format(bookName, pageLimit - 1)

    # 生成页面的地址
    bookPages = (url_pattern.format(x, str(i)) for i in range(1, pageLimit))
    # 生成图书保存页面
    bookSavePath = save_path + str(x)


    os.mkdir(bookSavePath)

    pageNo = 0

    for url in bookPages:
        pageNo += 1
        print(url)
        filePath = bookSavePath + "\\" + str(pageNo) + ".jpg"
        time.sleep(1)
        urlretrieve(url, filePath)

