# _*_ coding:utf-8 _*_

from bs4 import BeautifulSoup
import string

datas = [];
path = './index.html'
with open(path,'r') as web_data:
    # print(web_data.read())
    Soup = BeautifulSoup(web_data.read(),'lxml')
    thumbnails = Soup.find_all('div',{'class': 'thumbnail'})

for thumbnail in thumbnails:
    data = {
        'pic' : thumbnail.select("img")[0].get("src"),
        'title' : thumbnail.select("div.caption > h4 > a")[0].get_text(),
        'price' : thumbnail.select("div.caption > h4")[0].get_text(),
        'reviews' : thumbnail.select("div.ratings > p")[0].get_text().split()[0],
        'stars' : str(thumbnail.select("div.ratings > p:nth-of-type(2) > span"))
    }
    data['stars'] = data['stars'].replace("<span class=\"glyphicon glyphicon-star\"></span>",'★')
    data['stars'] = data['stars'].replace("<span class=\"glyphicon glyphicon-star-empty\"></span>",'☆')
    data['stars'] = data['stars'].replace('[','').replace(']','')
    datas.append(data)
    print(data)


