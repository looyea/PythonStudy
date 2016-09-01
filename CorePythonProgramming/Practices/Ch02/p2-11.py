# _*_ coding:utf-8 _*_
"""
带文本菜单的程序写一个带文本菜单的程序，菜单项如下：
（1）取五个数的和；（2）取五个数的平均值…（X）退出。
由用户做一个选择，然后执行相应的功能。当用户选择退出时程序结束。
这个程序的有用之处在于用户在功能之间切换不需要一遍一遍地重新启动
你的脚本（这对开发人员测试自己的程序也会大有用处）。
"""
atuple = (2,2,3,4,7)
def printMenu():
    print "当前数组: ", atuple
    print "1. 取五个数的和"
    print "2. 取五个数的平均值"
    print "X. 退出"

def sumTuple():
    sum = 0
    for x in atuple:
        sum += x
    print "总和是: ", sum
    return sum

def avgTuple():
    sum = sumTuple()
    print "平均数是: ", float(sum) / 5

while True:
    printMenu()
    choice = raw_input("请选择: ")
    if choice == "1":
        sumTuple()
    elif choice == "2":
        avgTuple()
    elif choice == "x" or choice == "X":
        break



