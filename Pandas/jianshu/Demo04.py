# _*_ coding:utf-8 _*_
import pandas as pd
import numpy as np


# Test 1
# 定义数据
dates = pd.date_range('20170101', periods = 6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index = dates, columns = ['A', 'B', 'C', 'D'])

# 假设缺少数据
df.iloc[1, 1] = np.nan
df.iloc[2, 2] = np.nan
print(df)

# Test 1 result
#              A     B     C   D
# 2017-01-01   0   1.0   2.0   3
# 2017-01-02   4   NaN   6.0   7
# 2017-01-03   8   9.0   NaN  11
# 2017-01-04  12  13.0  14.0  15
# 2017-01-05  16  17.0  18.0  19
# 2017-01-06  20  21.0  22.0  23

# Test 2
# 按行或列来舍弃数据, how = any or all, any是默认值
print(df.dropna(axis = 0, how = 'any'))

# 填充数据
print(df.fillna(value = 0))

# 判断是否缺失数据
print(df.isnull())

# 判断是否存在缺失数据的情况
print(np.any(df.isnull() == True))

# Test 2 result
#              A     B     C   D
# 2017-01-01   0   1.0   2.0   3
# 2017-01-04  12  13.0  14.0  15
# 2017-01-05  16  17.0  18.0  19
# 2017-01-06  20  21.0  22.0  23
#
#              A     B     C   D
# 2017-01-01   0   1.0   2.0   3
# 2017-01-02   4   0.0   6.0   7
# 2017-01-03   8   9.0   0.0  11
# 2017-01-04  12  13.0  14.0  15
# 2017-01-05  16  17.0  18.0  19
# 2017-01-06  20  21.0  22.0  23
#
#                 A      B      C      D
# 2017-01-01  False  False  False  False
# 2017-01-02  False   True  False  False
# 2017-01-03  False  False   True  False
# 2017-01-04  False  False  False  False
# 2017-01-05  False  False  False  False
# 2017-01-06  False  False  False  False
#
# True