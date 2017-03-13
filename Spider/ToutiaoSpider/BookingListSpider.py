# _*_ coding:utf-8 _*_

from bs4 import BeautifulSoup
import requests
import pymongo


HttpHeaders = {
    "Cookie": 'concern=a%3A1%3A%7Bs%3A9%3A%22stock%2Fzs%2F%22%3Bs%3A24%3A%22%25D6%25B8%25CA%25FD%25C1%25D0%25B1%25ED%22%3B%7D; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1480400472,1480402946,1480487513',
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36'
}

