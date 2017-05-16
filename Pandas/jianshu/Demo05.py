# _*_ coding:utf-8 _*_
import pandas as pd
import numpy as np

# Test 1
# 读取csv文件, sep指定字符串的分隔符, 默认为逗号
data = pd.read_csv('student.csv', sep = ';')
print(data)

# Test 1 result
#    Student ID   name  age  gender
# 0        1000   Jack   21    Male
# 1        1001   Lucy   22  Female
# 2        1002   Rose   23  Female
# 3        1003  David   24    Male


# Test 2
# 导出数据
data.to_pickle('student.pickle')

# Test 2 result
# 在目录下会看到student.pickle文件