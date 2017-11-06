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

baseDirStr = "/data/toProcess"
baseDirs = os.listdir(baseDirStr)
baseDirs.sort()

for dir in baseDirs:
    print("Start work with ", baseDirStr, dir)
    saveDir = baseDirStr + "/" + dir + "/" + dir
    if os.path.exists(saveDir):
        pass
    else:
        os.mkdir(saveDir)
    files = os.listdir(baseDirStr + "/" + dir + "/")
    counter = 1
    for file in files:
        curPath = baseDirStr + "/" + dir + "/" + file
        if os.path.isdir(curPath):
            continue

        if file == "dinfo" or file == "_image_info_list" or file == "imgs":
            pass
        else:
            url = retriveUrl(curPath)
            finalPath = saveDir +  "/" + str(counter) + ".jpg"
            request.urlretrieve(url, finalPath)
            counter += 1

        time.sleep(0.5)
