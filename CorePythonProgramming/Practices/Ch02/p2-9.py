# _*_ coding:utf-8 _*_
"""
循环和操作符。创建一个包含五个固定数值的列表或元组，输出他们的平均值。
本练习的难点之一是通过除法得到平均值。
你会发现整型除会截去小数，因此你必须使用浮点除以得到更精确的结果。
float()内建函数可以帮助你实现这一功能。
"""

atuple = (2,2,3,4,7);
sum = 0.0;
for x in atuple:
    sum += x
averageNumber = float(sum) / 5.0
print "average is %.2f " % averageNumber