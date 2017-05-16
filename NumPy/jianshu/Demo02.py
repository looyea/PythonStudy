# _*_ coding:utf-8 _*_
import numpy as np

# Test 1
a = np.arange(2, 14).reshape(3, 4)
print a

# Test 1 result
[[ 2  3  4  5]
 [ 6  7  8  9]
 [10 11 12 13]]

# Test 2
# 计算矩阵最小值的索引
print np.argmin(a)
# 计算矩阵最大值的索引
print np.argmax(a)
# 计算矩阵的均值
print np.mean(a)
print a.mean()
print np.average(a)
# 计算矩阵的中位数
print np.median(a)
# 计算前n项之和
print np.cumsum(a)
# 计算相邻两位的差
print np.diff(a)
# 找出非零的数, 输出的是非零数的索引，分别为行的索引和列的索引
print np.nonzero(a)

# Test 2 result
11
0
8.5
8.5
8.5
8.5
[ 14  27  39  50  60  69  77  84  90  95  99 102]
[[-1 -1 -1]
 [-1 -1 -1]
 [-1 -1 -1]]
(array([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]), array([0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]))

# Test 3
a = np.arange(14, 2, -1).reshape(3, 4)
print a
# 矩阵排序，按行排序
print np.sort(a)
# 矩阵的转置
print np.transpose(a)
print a.transpose()
print a.T

print a.T.dot(a)

# Test 3 result
[[14 13 12 11]
 [10  9  8  7]
 [ 6  5  4  3]]
[[11 12 13 14]
 [ 7  8  9 10]
 [ 3  4  5  6]]
[[14 10  6]
 [13  9  5]
 [12  8  4]
 [11  7  3]]
[[14 10  6]
 [13  9  5]
 [12  8  4]
 [11  7  3]]
[[14 10  6]
 [13  9  5]
 [12  8  4]
 [11  7  3]]
[[332 302 272 242]
 [302 275 248 221]
 [272 248 224 200]
 [242 221 200 179]]

# Test 4
print a
# 矩阵的处理，所有小于5的数等于5，所有大于10的数等于10
print np.clip(a, 5, 10)

# 计算矩阵指定维度的均值, 0是列, 1是行
print np.mean(a, axis = 0)

# Test 4 result
[[14 13 12 11]
 [10  9  8  7]
 [ 6  5  4  3]]
[[10 10 10 10]
 [10  9  8  7]
 [ 6  5  5  5]]
[ 10.   9.   8.   7.]