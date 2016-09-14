# _*_ coding:utf-8 _*_
"""
变量，print和字符串格式化操作符。启动交互式解释器，给一些变量赋值（字符串，数值等）
并通过输入变量名显示它们的值。
再用print语句做同样的事。这二者有何区别？
也尝试着使用字符串格式操作符%，多做几次，慢慢熟悉它。
"""

str1 = "a string"
int1 = 11
str1 # 会打印出'a string'
int1 # 会打印出11
print str1 # 会打印出a string, 不带引号
print int1 # 会打印出11
print "the string is %s and the number is %d" % (str1, int1)