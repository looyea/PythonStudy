# _*_ coding:utf-8 _*_
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 定义DataFrame
data = pd.DataFrame(np.random.randn(1000, 4), index = np.arange(1000), columns = list('ABCD'))
print(data)
# 累加数据
data = data.cumsum()
# print data
# 绘制数据
data.plot()
# 显示数据
plt.show()