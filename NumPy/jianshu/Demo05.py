# _*_ coding:utf-8 _*_
import numpy as np

# Test 1
A = np.arange(12).reshape(3, 4)
print(A)

# 纵向分割, 分成两部分, 按列分割
print(np.split(A, 2, axis = 1))
# 横向分割, 分成三部分, 按行分割
print(np.split(A, 3, axis = 0))

# Test 1 result
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
# [array([[0, 1],
#        [4, 5],
#        [8, 9]]), array([[ 2,  3],
#        [ 6,  7],
#        [10, 11]])]
# [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]

# Test 2
# 不均等分割
print(np.array_split(A, 3, axis = 1))

# Test 2 result
# [array([[0, 1],
#        [4, 5],
#        [8, 9]]), array([[ 2],
#        [ 6],
#        [10]]), array([[ 3],
#        [ 7],
#        [11]])]
# In [5]:

# Test 3
# 垂直方向分割
print(np.vsplit(A, 3))
# 水平方向分割
print(np.hsplit(A, 2))

# Test 3 result
# [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]
# [array([[0, 1],
#        [4, 5],
#        [8, 9]]), array([[ 2,  3],
#        [ 6,  7],
#        [10, 11]])]