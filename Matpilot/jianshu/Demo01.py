# _*_ coding:utf-8 _*_

import matplotlib.pyplot as plt
import numpy as np

# 绘制普通图像
x = np.linspace(-1, 1, 50)
y = 2 * x + 1
plt.plot(x, y)
plt.show()

# 绘制普通图像
y = x**2
plt.plot(x, y)
plt.show()