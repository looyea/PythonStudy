# _*_ coding:utf-8 _*_

'''
这个程序是当初为了处理自然语言处理的标准库无法下载而编写的.
主要工作的内容就是, 将其中的URL提取出来, 可以直接复制URL组
这样, 可以让迅雷一次性的进行处理. 让百度直接下载, 非常方便
'''
from bs4 import BeautifulSoup
import requests




link = 'https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/index.xml'

web_data = requests.get(link)
soup = BeautifulSoup(web_data.text,'lxml')
pkgs = soup.findAll("package")
urls = list()
for pkg in pkgs:
    print(pkg['url'])

