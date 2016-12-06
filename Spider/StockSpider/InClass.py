# _*_ coding:utf-8 _*_

from bs4 import BeautifulSoup
import requests
import time

stocks = []
headers = {
    "Cookie" : 'concern=a%3A1%3A%7Bs%3A9%3A%22stock%2Fzs%2F%22%3Bs%3A24%3A%22%25D6%25B8%25CA%25FD%25C1%25D0%25B1%25ED%22%3B%7D; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1480400472,1480402946,1480487513',
    "User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36'
}

# 原来的数据是针对tripadvisor.com, 这里我们针对同花顺, 爬股票信息
urls = ('http://q.10jqka.com.cn/index/index/board/hs/field/zdf/order/desc/page/{}/ajax/1/'.format(str(i)) for i in range(1,54) )
def get_page_data(url, headers = None):
    print(url)
    web_data = requests.get(url, headers)
    Soup = BeautifulSoup(web_data.text, 'lxml');
    infos = Soup.select("tbody > tr")

    for info in infos:
        info_list = info.get_text().split('\n')
        stock = {
            'sequenceNao'     : info_list[1], #  序号
            'stockCode'       : info_list[2], # 代码
            'stockName'       : info_list[3], # 名称
            'curPrice'        : info_list[4], # 现价
            'riseFallRatio'   : info_list[5],  # 涨跌幅
            'riseFallPrice'   : info_list[6],  # 涨跌
            'riseFallRate'    : info_list[7],    # 涨速
            'exchangePercent' : info_list[8], # 换手比
            'amountRatio'     : info_list[9], # 量比
            'amplifier'       : info_list[10], # 振幅
            'turnover'        : info_list[11], # 成交额
            'spareStock'      : info_list[12], # 流通股
            'spareVolume'     : info_list[13], # 流通市值
            'benefits'        : info_list[14], # 市盈率
        }
        stocks.append(stock)

for url in urls:
    get_page_data(url, headers)


print(len(stocks))