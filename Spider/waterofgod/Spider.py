# _*_ coding:utf-8 _*_

'''
为了爬取神之水滴的漫画做的东西
首先需要你本地下载了腾讯的漫画，然后提取出离线的文件
这个程序就是针对离线文件进行处理的
'''

import os
import time
import urllib
import sys
import os
import codecs


def retriveUrl(file):
    with codecs.open(file, 'r+', 'GBK', 'ignore') as f:
        line = f.readline()
        start = line.index("http:")
        end = line.index(".jpg") + 4
        return line[start: end]

baseDirStr = "/media/appadmin/Work/qqcomics/546289"
baseDirs = os.listdir(baseDirStr)
baseDirList = ((baseDirStr + "/{}/").format(dir) for dir in baseDirs)

for dir in baseDirList:
    files = os.listdir(dir)
    for file in files:
        if file == "dinfo" or file == "_image_info_list":
            pass
        else:
            url = retriveUrl(dir + file)
            print(url)
