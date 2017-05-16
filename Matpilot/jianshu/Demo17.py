# _*_ coding:utf-8 _*_
import matplotlib.pyplot as plt

# 划分figure
fig, ((ax11, ax12), (ax21, ax22)) = plt.subplots(2, 2, sharex = True, sharey = True)

# 绘制图像
ax11.scatter([0, 0.5], [0, 1])
ax12.scatter([0, 1], [0, 1])
ax21.scatter([0, 1], [0, -1])
ax22.scatter([0, -1], [0, 1])
plt.show()