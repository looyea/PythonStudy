# _*_ coding:utf-8 _*_
import numpy as np

# Test 1
a = np.arange(4)
print(a)

# 直接赋值, a,b,c,d是同一个array
b = a
c = a
d = b
a[0] = 10
print(b is a)
print(c is a)
print(d is a)

# Test 1 result
# [0 1 2 3]
# True
# True
# True

# Test 2
# 深拷贝
b = a.copy()
b[0] = 12
print(b is a)
print(a)
print(b)

# Test 2 result
# False
# [10  1  2  3]
# [12  1  2  3]