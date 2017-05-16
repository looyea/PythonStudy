# _*_ coding:utf-8 _*_
import numpy as np

# Test 1
# 定义矩阵
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(arr)

# Test 1 Result
# [[1 2 3]
#  [4 5 6]]

# Test 2
# 矩阵的维度
print('number of dim: ', arr.ndim)
# 矩阵的shape,即每一维度上的元素个数
print('shape: ', arr.shape)
# 矩阵的元素总数
print('size: ', arr.size)
# 矩阵的元素类型
print('dtype: ', arr.dtype)

# Test 2 Result
# number of dim:  2
# shape:  (2, 3)
# size:  6
# dtype:  int64

# Test 3
# 定义矩阵及矩阵的元素类型——int32, int64, float32, float64
a = np.array([1, 2, 3], dtype = np.int32)
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)


# Test 3 Result
# [1 2 3]
# 1
# (3,)
# 3
# int32

# Test 4
# 定义零矩阵
z = np.zeros((3, 4), dtype = np.int16)
print(z)
print(z.dtype)

# 定义空矩阵
n = np.empty((3, 4))
print(n)

# Test 4 Result
# [[0 0 0 0]
#  [0 0 0 0]
#  [0 0 0 0]]
# int16
#
# [[ 0.  0.  0.  0.]
#  [ 0.  0.  0.  0.]
#  [ 0.  0.  0.  0.]]

# Test 5
# 定义向量, 10-20之间, 元素间隔为2, 左闭右开
a = np.arange(10, 20, 2)
print(a)

# 定义向量并转为矩阵
b = np.arange(12).reshape((3, 4))
print(b)

# 定义向量, 类型是线性间隔
a = np.linspace(1, 10, 6).reshape((2, 3))
print(a)

# Test 5 Result
# [10 12 14 16 18]
#
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
#
# [[  1.    2.8   4.6]
#  [  6.4   8.2  10. ]]

# Test 6
# 矩阵的加、减、点乘、平方
a = np.array([10, 20, 30, 40])
b = np.arange(4)
c = a - b
d = a + b
print(a, b)
print(c, d)
e = a * b
print(e)
f = e ** 2
print(f)

# Test 6 Result
# [10 20 30 40] [0 1 2 3]
# [10 19 28 37] [10 21 32 43]
# [  0  20  60 120]
# [    0   400  3600 14400]

# Test 7
# 矩阵的三角运算——sin, cos, tan
sin = 10 * np.sin(a)
print(sin)

# 矩阵的判断
print(b < 3)
print(b == 3)

# Test 7 Result
# [-5.44021111  9.12945251 -9.88031624  7.4511316 ]
#
# [ True  True  True False]
# [False False False  True]

# Test 8
# 矩阵的点乘及乘法
a = [ [1, 1], [0, 1]]
b = np.arange(4).reshape((2, 2))
c = a * b
d = np.dot(a, b)
print(c)
print(d)

# Test 8 Result
# [[0 1]
#  [0 3]]
# [[2 4]
#  [2 3]]

# Test 9
# np.random返回随机的浮点数，在半开区间 [0.0, 1.0)
# 定义随机矩阵
a = np.random.random((2, 4))
print(a)

# Test 9 Result
# [[ 0.93213483  0.58102186  0.98259187  0.27387014]
#  [ 0.43796835  0.98195976  0.29343791  0.94752226]]

# Test 10
# 矩阵的求和, 最小值, 最大值
print(np.sum(a))
print(np.min(a))
print(np.max(a))

# 矩阵某一维度的求和, 最小值, 最大值, 0是列, 1是行
print(np.sum(a, axis = 1))
print(np.max(a, axis = 1))
print(np.min(a, axis = 0))

# Test 10 Result
# 5.43050697485
# 0.273870140282
# 0.982591870104
#
# [ 2.7696187   2.66088828]
# [ 0.98259187  0.98195976]
# [ 0.43796835  0.58102186  0.29343791  0.27387014]