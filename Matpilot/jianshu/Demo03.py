# _*_ coding:utf-8 _*_

import matplotlib.pyplot as plt
import numpy as np

# 绘制普通图像
x = np.linspace(-1, 1, 50)
y1 = 2 * x + 1
y2 = x**2

plt.figure()
plt.plot(x, y1)
plt.plot(x, y2, color = 'red', linewidth = 1.0, linestyle = '--')

# 设置坐标轴的取值范围
plt.xlim((-1, 1))
plt.ylim((0, 2))

# 设置坐标轴的lable
plt.xlabel('X axis')
plt.ylabel('Y axis')

# 设置x坐标轴刻度, 原来为0.25, 修改后为0.5
plt.xticks(np.linspace(-1, 1, 5))
# 设置y坐标轴刻度及标签, $$是设置字体
plt.yticks([0, 0.5], ['$minimum$', 'normal'])

plt.show()