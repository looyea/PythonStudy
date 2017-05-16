# _*_ coding:utf-8 _*_
import pandas as pd
import numpy as np

# Test 1
# 定义序列, pandas中的数据形式通常是float32或float64
s = pd.Series([1, 3, 5, np.nan, 44,  1])
print s
print s[0]
print s[3]

# Test 1 result
0     1.0
1     3.0
2     5.0
3     NaN
4    44.0
5     1.0
dtype: float64
1.0
nan

# Test 2
# 定义日期列表
dates = pd.date_range('20170101', periods = 6)
print dates
print dates[5]

# Test 2 result
DatetimeIndex(['2017-01-01', '2017-01-02', '2017-01-03', '2017-01-04',
               '2017-01-05', '2017-01-06'],
              dtype='datetime64[ns]', freq='D')
2017-01-06 00:00:00

# Test 3
# DataFrame类似于numpy的array, 行索引为dates, 列索引为[a, b, c, d]
df = pd.DataFrame(np.random.randn(6, 4), index = dates, columns = ['a', 'b', 'c', 'd'])
print df

# 不指定索引的DataFrame
df = pd.DataFrame(np.arange(12).reshape(3, 4))
print df

# DataFrame的定义
df = pd.DataFrame({'A': 1., 'B': 'Foo', 'C': np.array([3] * 4)})
print df

# Test 3 result
                   a         b         c         d
2017-01-01  1.104994  1.328379  0.410358 -1.661059
2017-01-02 -0.642727 -0.152576  1.126191 -0.005317
2017-01-03 -0.179257  0.160972 -0.824172 -0.175027
2017-01-04  0.838328 -0.500909  0.714592  1.144800
2017-01-05  0.803691 -3.979186 -1.037603 -0.747943
2017-01-06  1.217289 -0.074413  0.504138 -0.077507

   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11

     A    B  C
0  1.0  Foo  3
1  1.0  Foo  3
2  1.0  Foo  3
3  1.0  Foo  3

# Test 4
# 查看DataFrame的数据类型
df.dtypes

# 查看DataFrame的索引
df.index

# 查看DataFrame的列索引
df.columns

# 查看DataFrame的值
df.values

# 查看DataFrame的描述
df.describe()

# DataFrame的转置
df.T

# DataFrame的index排序
df.sort_index(axis = 1)

# DataFrame的index排序, 逆序
df.sort_index(axis = 1, ascending = False)

# DataFrame按值排序
df.sort_values(by = 'C')

# Test 4 result
A    float64
B     object
C      int64
dtype: object

RangeIndex(start=0, stop=4, step=1)

Index([u'A', u'B', u'C'], dtype='object')

array([[1.0, 'Foo', 3],
       [1.0, 'Foo', 3],
       [1.0, 'Foo', 3],
       [1.0, 'Foo', 3]], dtype=object)

       A      C
count  4.0    4.0
mean   1.0    3.0
std    0.0    0.0
min    1.0    3.0
25%    1.0    3.0
50%    1.0    3.0
75%    1.0    3.0
max    1.0    3.0

       0      1      2      3
A      1      1      1      1
B      Foo    Foo    Foo    Foo
C      3      3      3      3


       A      B      C
0      1.0    3      Foo
1      1.0    3      Foo
2      1.0    3      Foo
3      1.0    3      Foo

       C      B      A
0      Foo    3      1.0
1      Foo    3      1.0
2      Foo    3      1.0
3      Foo    3      1.0

       A      B      C
0      1.0    3      Foo
1      1.0    3      Foo
2      1.0    3      Foo
3      1.0    3      Foo