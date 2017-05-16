# _*_ coding:utf-8 _*_
import numpy as np

# Test 1
# 一维矩阵
a = np.arange(3, 15)
print(a)
# 输出矩阵的第三个元素
print(a[2])

# Test 1 result
# [ 3  4  5  6  7  8  9 10 11 12 13 14]
# 5

# Test 2
# 二维矩阵
a = np.arange(3, 15).reshape(3, 4)
print(a)
# 输出矩阵的第二行
print(a[1])
# 输出矩阵的第一个元素
print(a[0][0])
# 输出矩阵某个位置上的元素
print(a[2][1])
print(a[2, 1])
# 输出矩阵第三行的所有数字
# :代表整行或整列
print(a[2, :])
# 输出矩阵第二行的前三个数，左开右闭
print(a[1, 0:3])

# Test 2 result
# [[ 3  4  5  6]
#  [ 7  8  9 10]
#  [11 12 13 14]]
# [ 7  8  9 10]
# 3
# 12
# 12
# [11 12 13 14]
# [7 8 9]

# Test 3
# 迭代矩阵的行
for row in a:
    print(row)

# 迭代矩阵的列
for column in a.T:
    print(column)

# Test 3 result
# [3 4 5 6]
# [ 7  8  9 10]
# [11 12 13 14]
#
# [ 3  7 11]
# [ 4  8 12]
# [ 5  9 13]
# [ 6 10 14]

# Test 4
# 矩阵展开
print(a.flatten())
# 迭代矩阵的元素
for item in a.flat:
    print(item)

# Test 4 result
# [ 3  4  5  6  7  8  9 10 11 12 13 14]
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14