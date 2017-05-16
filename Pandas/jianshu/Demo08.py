# _*_ coding:utf-8 _*_
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 定义Series
data = pd.Series(np.random.randn(1000), index = np.arange(1000))
print(data)
# 累加数据
data = data.cumsum()
# 绘制数据
data.plot()
# 显示数据
plt.show()