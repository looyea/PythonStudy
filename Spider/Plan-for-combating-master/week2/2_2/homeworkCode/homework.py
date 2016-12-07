# _*_ coding:utf-8 _*_
from bs4 import BeautifulSoup
import requests
import pymongo
import string

url = "http://bj.58.com/shoujihao"
headers = {
    "Cookie" : "f=n; ipcity=bj%7C%u5317%u4EAC; webps=A; id58=c5/nn1eDGe9nb48iHth1Ag==; 58home=bj; bj58_id58s=\"WWNDRXI3enVfZ3VjMDYwOQ==\"; als=0; bdshare_firstime=1481010755905; myfeet_tooltip=end; bangbigtip2=1; final_history=28276771296201%2C27911240984379%2C26088204291258; city=bj; f=n; bj58_new_session=1; bj58_init_refer=""; bj58_new_uv=2; sessionid=00d3c502-b092-47af-ab09-a4631f9cf998; Hm_lvt_ef9ab733a6772ffc77e498ec3aee46bd=1481092118; Hm_lpvt_ef9ab733a6772ffc77e498ec3aee46bd=1481092118; 58tj_uuid=78c275b9-279f-4cf7-b724-252e7c141611; new_session=1; new_uv=2; utm_source=; spm=; init_refer=",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36"
}

def getSoupObj(url, headers = None):
    web_data = requests.get(url, headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    return soup

def getMongoDbObj():
    client = pymongo.MongoClient("localhost", 27017)
    testDb = client['testdb']
    cellNumbers = testDb['CellNumbers']
    return cellNumbers

def parsingCellNumber(soupObj, mongoSheet):
    phoneNumbers = soupObj.findAll("a", {"class":"t"})
    for ph in phoneNumbers:
        no = ph.find("strong", {"class":"number"}).get_text()
        title = ph.find("span", {"class": "jz-title"})
        if ( None != title):
            title = title.get_text()
        else:
            title = ph.find("span").get_text().strip()

        print(title)
        number = {
            "no" : no,
            "title" : title
        }
        mongoSheet.insert_one(number)


soup = getSoupObj(url, headers)
mongoSheet = getMongoDbObj()

parsingCellNumber(soup, mongoSheet)