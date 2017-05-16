# _*_ coding:utf-8 _*_
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.DataFrame(np.random.randn(100, 4), index = np.arange(100), columns = list('ABCD'))
# 绘制散点图
ax = data.plot.scatter(x = 'A', y = 'B', color = 'DarkBlue')
data.plot.scatter(x = 'A', y = 'C', color = 'DarkGreen', ax = ax)
plt.show()