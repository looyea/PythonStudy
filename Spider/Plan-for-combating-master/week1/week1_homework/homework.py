# _*_ coding:utf-8 _*_

from bs4 import BeautifulSoup
from urllib2 import HTTPError
import time
import requests

urls = ['http://bj.58.com/pbdn/{}/'.format(str(i)) for i in range(0,5)]
headers = {
    "Cookie" : "f=n; ipcity=bj%7C%u5317%u4EAC; myfeet_tooltip=end; f=n; id58=c5/nn1eDGe9nb48iHth1Ag==; 58home=bj; bj58_new_session=1; bj58_init_refer=""; bj58_new_uv=1; bj58_id58s=\"WWNDRXI3enVfZ3VjMDYwOQ==\"; sessionid=771919ef-7f22-4dd9-9abc-132b77c37466; f=n; 58tj_uuid=78c275b9-279f-4cf7-b724-252e7c141611; new_session=1; new_uv=1; utm_source=; spm=; init_refer=; als=0",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36"
}
tablets = []


def getSoupObj(url, headers):
    time.sleep(1)
    web_data = requests.get(url, headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    return soup

def parsingItemInfo(url, headers = None):
    print("解析页面: " +  url)
    try:
        soup = getSoupObj(url, headers)
        cates = soup.select("span.crb_i")
        cate = cates[ - len(cates)].get_text()
        title = soup.select("body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.box_left_top > h1")[0].get_text()
        price = soup.select("span.price_now > i")[0].get_text()
        region = soup.select("div.palce_li > span > i")[0].get_text()
        reviews = soup.select("span.look_time")[0].get_text().replace(u'次浏览','')

        tablet = {
            "cate" : cate,
            "title" : title,
            "price" : price,
            "region" : region,
            "reviews" : reviews
        }
        tablets.append(tablet)
        print("获取到商品: " + title)

    except (HTTPError, AttributeError) as e:
        print(e, url)



def parsingTabletInfo(url, headers = None):
    links = []
    soup = getSoupObj(url, headers)
    aTags = soup.select("tr.zzinfo > td.t > a.t")
    for aTag in aTags:
        link = aTag.get("href")
        # links.append(link)
        parsingItemInfo(link, headers)


# parsingItemInfo("http://zhuanzhuan.58.com/detail/756051329702608900z.shtml?fullCate=5%2C38484%2C23094&fullLocal=1&from=pc", headers)

print("解析页面开始.....")
for url in urls:
    parsingTabletInfo(url, headers)

print(" ------ 解析网页完毕 ------ ")


