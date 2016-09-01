# _*_ coding:utf-8 _*_
"""
条件判断。判断一个数是正数，还是负数，或者是0。开始先用固定的数值，然后修改你的代码支持用户输入数值再进行判断。
"""
anum = input("input a number: ")
if anum > 0:
    print "a positive number"
elif anum < 0:
    print "a negative number"
else:
    print "a zero"