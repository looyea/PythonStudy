# _*_ coding:utf-8 _*_
"""
文件。键入2.15节的文件显示的代码，然后运行它，看看能否在你的系统上正常工作，然后试一下其他的输入文件。
"""

filename = raw_input('Enter file name: ')
fobj = open(filename, 'r')
for eachLine in fobj:
    print eachLine
fobj.close()