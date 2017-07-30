# _*_ coding:utf-8 _*_

import time
import requests
from bs4 import BeautifulSoup
import pdfkit



urls = ["http://bbs.quanttech.cn/article/{:0>3}".format(str(i))  for i in range(700)]
topicNos = [i for i in range(700)]



def htmlComposer(header, content):
    htmlHead = '''
    <html>
        <head>
            <meta content="text/html;charset=utf-8" http-equiv="Content-Type" />
            <link href="http://bbs.quanttech.cn/static/css/default/common.css?v=20150226" rel="stylesheet" type="text/css" />
            <link href="http://bbs.quanttech.cn/static/css/default/link.css?v=20150226" rel="stylesheet" type="text/css" />
            <style>
            
            </style>
        </head>
        <body>
    '''

    htmlTail = '''
        </body>
    </html>
    '''

    htmlStr = htmlHead + "<h1>" + header + "</h1>"
    for data in content:
        htmlStr += str(data)

    htmlStr = htmlStr + htmlTail
    return htmlStr

def htmlPaser(soup):
    title = soup.select('h2.userask')
    title = title[0].contents[0]
    content = soup.select('div.content')
    htmlStr = htmlComposer(title, content)
    return {"title": title, "content": htmlStr}



for enum in enumerate(topicNos):
    try:

        url = urls[enum[0]]

        web_data = requests.get(url, allow_redirects=False)
        if web_data.status_code != 200:
            print("Pass " + url)
            continue
        Soup = BeautifulSoup(web_data.text, 'lxml')

        print("processing "+ url)
        noStr = "{:0>3}".format(enum[0])
        data = htmlPaser(Soup)
        pdfkit.from_string(data["content"], "D:\\quanttech\\" + noStr + '_' + data["title"] + ".pdf")
        time.sleep(1)
    except Exception  :
        print(Exception)
        continue