# _*_ coding:utf-8 _*_
"""
带循环和条件判断的用户输入。
使用raw_input0函数来提示用户输入一个1和100之间的数，如果用户输入的数满足这个条件，
显示成功并退出。
否则显示一个错误信息然后再次提示用户输入数值，直到满足条件为止。
"""

theNum = raw_input("please input a number: ")
if (theNum.isdigit()):
    num = int(theNum)
    if 1<= num <= 100:
        print "OK!"
    else:
        print "no good!"
else:
    print "plese input a number not others."