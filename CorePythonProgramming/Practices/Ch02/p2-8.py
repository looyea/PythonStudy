# _*_ coding:utf-8 _*_
"""
循环和操作符。创建一个包含五个固定数值的列表或元组，输出他们的和。然后修改你的代码为接受用户输入数值。分别使用while和for循环实现。
"""

astr = raw_input("please input a string: ")
for x in astr:
    print x,

print
i = 0
len = len(astr)
while i < len:
    print astr[i],
    i+= 1


