# _*_ coding:utf-8 _*_
import pandas as pd
import numpy as np


# Test 1
# 定义数据
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                    'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']})

print(left)
print(right)

# merge合并
res = pd.merge(left, right, on = 'key')
print(res)

# Test 1 result
#     A   B key
# 0  A0  B0  K0
# 1  A1  B1  K1
# 2  A2  B2  K2
# 3  A3  B3  K3
#     C   D key
# 0  C0  D0  K0
# 1  C1  D1  K1
# 2  C2  D2  K2
# 3  C3  D3  K3
# 
#     A   B key   C   D
# 0  A0  B0  K0  C0  D0
# 1  A1  B1  K1  C1  D1
# 2  A2  B2  K2  C2  D2
# 3  A3  B3  K3  C3  D3

# Test 2
# 定义数据
left = pd.DataFrame({'key1': ['K0', 'K1', 'K2', 'K3'],
                     'key2': ['K0', 'K1', 'K2', 'K3'],
                    'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K2', 'K3'],
                      'key2': ['K0', 'K1', 'K2', 'K4'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']})

print(left)
print(right)
# 合并两列, 默认方法是how=inner, 只合并相同的部分, how的取值可以为['left', 'right', 'outer', 'inner']
res = pd.merge(left, right, on = ['key1', 'key2'])
print(res)

# Test 2 result
#     A   B key1 key2
# 0  A0  B0   K0   K0
# 1  A1  B1   K1   K1
# 2  A2  B2   K2   K2
# 3  A3  B3   K3   K3
#     C   D key1 key2
# 0  C0  D0   K0   K0
# 1  C1  D1   K1   K1
# 2  C2  D2   K2   K2
# 3  C3  D3   K3   K4
#     A   B key1 key2   C   D
# 0  A0  B0   K0   K0  C0  D0
# 1  A1  B1   K1   K1  C1  D1
# 2  A2  B2   K2   K2  C2  D2

# Test 3
# 通过indicator表明merge的方式
res = pd.merge(left, right, on = ['key1', 'key2'], how = 'outer', indicator = True)
print(res)

# 修改indicator的名字
res = pd.merge(left, right, on = ['key1', 'key2'], how = 'outer', indicator = 'indicator')
print(res)

# Test 3 result
#      A    B key1 key2    C    D      _merge
# 0   A0   B0   K0   K0   C0   D0        both
# 1   A1   B1   K1   K1   C1   D1        both
# 2   A2   B2   K2   K2   C2   D2        both
# 3   A3   B3   K3   K3  NaN  NaN   left_only
# 4  NaN  NaN   K3   K4   C3   D3  right_only
# 
#      A    B key1 key2    C    D   indicator
# 0   A0   B0   K0   K0   C0   D0        both
# 1   A1   B1   K1   K1   C1   D1        both
# 2   A2   B2   K2   K2   C2   D2        both
# 3   A3   B3   K3   K3  NaN  NaN   left_only
# 4  NaN  NaN   K3   K4   C3   D3  right_only

# Test 4
# 定义数据
left = pd.DataFrame({ 'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']},
                      index = ['K0', 'K1', 'K2', 'K3'])
right = pd.DataFrame({'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']},
                      index = ['K0', 'K1', 'K2', 'K3'])

print(left)
print(right)

# merge数据
res = pd.merge(left, right, left_index = True, right_index = True, how = 'outer')
print(res)

# Test 4 result
#      A   B
# K0  A0  B0
# K1  A1  B1
# K2  A2  B2
# K3  A3  B3
#      C   D
# K0  C0  D0
# K1  C1  D1
# K2  C2  D2
# K3  C3  D3
#
#      A   B   C   D
# K0  A0  B0  C0  D0
# K1  A1  B1  C1  D1
# K2  A2  B2  C2  D2
# K3  A3  B3  C3  D3

# Test 5
# 定义数据
left = pd.DataFrame({ 'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['D0', 'D1', 'D2', 'D3']})

print(left)
print(right)

# 区分两个B
res = pd.merge(left, right, on = 'A', how = 'inner', suffixes = ['_left', '_right'])
print(res)

# Test 5 result
#     A   B
# 0  A0  B0
# 1  A1  B1
# 2  A2  B2
# 3  A3  B3
#     A   B
# 0  A0  D0
# 1  A1  D1
# 2  A2  D2
# 3  A3  D3
#     A B_left B_right
# 0  A0     B0      D0
# 1  A1     B1      D1
# 2  A2     B2      D2
# 3  A3     B3      D3