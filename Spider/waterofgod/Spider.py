# _*_ coding:utf-8 _*_

'''
为了爬取神之水滴的漫画做的东西
首先需要你本地下载了腾讯的漫画，然后提取出离线的文件
这个程序就是针对离线文件进行处理的
'''

import os
import time
from urllib import request
import sys
import os
import codecs
import time


def retriveUrl(file):
    with codecs.open(file, 'r+', 'GBK', 'ignore') as f:
        line = f.readline()
        start = line.index("http:")
        end = line.index(".jpg") + 4
        return line[start: end]

headers = {
   "User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0'
}

baseDirStr = "/media/appadmin/Work/qqcomics/546289"
baseDirs = os.listdir(baseDirStr)
baseDirList = ((baseDirStr + "/{}/").format(dir) for dir in baseDirs)

for dir in baseDirList:
    print("Start work with ", dir)
    os.mkdir(dir + "/imgs")
    saveDir = dir + "/imgs/"
    files = os.listdir(dir)
    counter = 1
    for file in files:
        time.sleep(1)
        if file == "dinfo" or file == "_image_info_list" or file == "imgs":
            pass
        else:
            url = retriveUrl(dir + file)
            print(url)
            finalPath = saveDir + str(counter) + ".jpg"
            request.urlretrieve(url, finalPath)
            counter += 1
