# _*_ coding:utf-8 _*_

import numpy as np

# Test 1
A = np.array([1, 1, 1])
B = np.array([2, 2, 2])
# 合并array, 竖直方向
C = np.vstack((A, B))
print(A.shape)
print(C.shape)
print(C)

# 合并array, 水平方向
D = np.hstack((A, B))
print(A.shape)
print(D.shape)
print(D)

# Test 1 result
# (3,)
# (2, 3)
# [[1 1 1]
#  [2 2 2]]
# (3,)
# (6,)
# [1 1 1 2 2 2]

# Test 2
A = np.array([1, 1, 1])
# 添加维度
# 列方向上添加维度
B = A[:, np.newaxis]
print(A)
print(B)
print(A.shape)
print(B.shape)
# 行方向上添加维度
C = A[np.newaxis, :]
print(A)
print(C)
print(A.shape)
print(C.shape)

# Test 2 result
# [1 1 1]
# [[1]
#  [1]
#  [1]]
# (3,)
# (3, 1)
# [1 1 1]
# [[1 1 1]]
# (3,)
# (1, 3)

# Test 3
A = np.array([1, 1, 1])
B = np.array([2, 2, 2])
# A, B列方向添加维度
A = A[:, np.newaxis]
B = B[:, np.newaxis]
# 合并多个array并指定合并的维度, 列方向上合并
C = np.concatenate((A, B, B, A), axis = 0)
# 合并多个array并指定合并的维度, 行方向上合并
D = np.concatenate((A, B, B, A), axis = 1)
print(A)
print(B)
print(C)
print(D)

# Test 3 result
# [[1]
#  [1]
#  [1]]
# [[2]
#  [2]
#  [2]]
# [[1]
#  [1]
#  [1]
#  [2]
#  [2]
#  [2]
#  [2]
#  [2]
#  [2]
#  [1]
#  [1]
#  [1]]
# [[1 2 2 1]
#  [1 2 2 1]
#  [1 2 2 1]]