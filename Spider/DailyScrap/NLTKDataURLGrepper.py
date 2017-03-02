# _*_ coding:utf-8 _*_
from bs4 import BeautifulSoup
import requests


link = 'https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/index.xml'

web_data = requests.get(link)
soup = BeautifulSoup(web_data.text,'lxml')
pkgs = soup.findAll("package")
urls = list()
for pkg in pkgs:
    print(pkg['url'])

