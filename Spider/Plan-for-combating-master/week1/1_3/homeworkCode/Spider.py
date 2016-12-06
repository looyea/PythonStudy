# _*_ coding:utf-8 _*_
'''
原文爬取
http://bj.xiaozhu.com/search-duanzufang-p1-0/
现在此站点已经不在了, 经过跟踪, 数据连接使用JSONP的形式返回
http://wirelesspub.xiaozhu.com/app/xzfk/html5/500/search/result?jsonp=api_search_result&cityId=12&offset=20&length=5

去掉JSONP的参数, 直接得到这个连接:
http://wirelesspub.xiaozhu.com/app/xzfk/html5/500/search/result?cityId=12&offset=20&length=5

调用后返回的数据, 就是直接整理好的数据了!!!
具体格式见下面的代码,
当然我们这里的代码是网站返回得到的数据, 不能直接使用. 否则会出问题.

'''

aDict = {
    "status": 200,
    "content": {
        "count": 6000,
        "item": [
            {
                "luId": 5465434314,
                "luTitle": "十里堡青年路6号线朝阳北路朝阳大悦城温馨单间",
                "luLeaseType": "独立单间",
                "displayAddr": "朝阳朝阳雅筑",
                "luPrice": 148,
                "luComments": 7,
                "luMainImageUrl": "\/\/image.xiaozhustatic1.com\/12\/8,0,41,2464,1800,1200,87f7df33.jpg",
                "extImages": ["\/\/image.xiaozhustatic1.com\/12\/8,0,41,2464,1800,1200,87f7df33.jpg",
                              "\/\/image.xiaozhustatic1.com\/12\/8,0,85,2368,1800,1200,c5838479.jpg",
                              "\/\/image.xiaozhustatic1.com\/12\/8,0,95,2370,1800,1200,2308de0c.jpg",
                              "\/\/image.xiaozhustatic1.com\/12\/8,0,4,2348,1800,1200,e504a39a.jpg",
                              "\/\/image.xiaozhustatic1.com\/12\/8,0,92,2425,1800,1200,0c7198cf.jpg",
                              "\/\/image.xiaozhustatic1.com\/12\/8,0,69,2447,1800,1200,65fee769.jpg",
                              "\/\/image.xiaozhustatic1.com\/12\/8,0,17,2361,1800,1200,2890e58c.jpg",
                              "\/\/image.xiaozhustatic1.com\/12\/8,0,97,2444,1800,1200,6bf1e2bf.jpg",
                              "\/\/image.xiaozhustatic1.com\/12\/8,0,20,2456,1800,1200,779a2179.jpg",
                              "\/\/image.xiaozhustatic1.com\/12\/8,0,16,2405,1800,1200,fe6f6f52.jpg"],
                "cashPledgeFree": 1,
                "isSuDing": 0,
                "isYouHui": 0,
                "isTejia": 0,
                "landlordheadimgurl": "\/\/image.xiaozhustatic1.com\/roundcrop\/6\/00,260,260,1,80,1\/8,0,70,1888,330,329,00261720.jpg",
                "landlordId": 5465152213,
                "yanzhen": true,
                "shipai": true,
                "landlordPersonRole": true,
                "realIdentity": true,
                "landlordName": "CarolSu",
                "promotionMonth": "",
                "promotionWeek": "",
                "isNew": false,
                "latitude": "39.929872",
                "longitude": "116.529925",
                "qualityNew": true,
                "isdoorlock": false,
                "commentScore": "5",
                "lodgeUnit4Label": ["qualityNew", "cashPledgeFree", "yanZhen", "shiPai"],
                "lodgeUnitTags": [1, 2, 3, 6, 9],
                "timezone": "+08:00",
                "localprice": 148,
                "currency": "CNY",
                "showPrice": {"pricePreTip": "", "price": "148", "priceTip": "", "startDate": "", "endDate": "",
                              "discountPreTip": "特价", "discount": "", "fiexdPrice": false, "first": true,
                              "originalPrice": "0",
                              "originalPriceTip": "原价", "localCurrency": "CNY", "currency": "¥", "currencyTip": "",
                              "priceUnitTip": "\/晚", "inCheckDate": false},
                "luPirce": "148",
                "promotioninfo": false
            }],
        "AmOperation": {"imageUrl": "", "url": "", "location": 5}
    }
}
