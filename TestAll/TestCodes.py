# _*_ coding:utf-8 _*_
from matplotlib import pyplot as plt
import numpy as np
import numpy.random as rd

def normal_pdf(mean, var, x):
    return 1 / np.sqrt(2 * np.pi * var) * np.exp(-(x - mean) ** 2 / (2 * var))


rd.seed(42)  # 种子值
data = rd.normal(0, 2.0, size=10)  # 产生10个正态分布的随机数
mean, var = np.mean(data), np.var(data)  # 计算最大似然估计的参数
var_range = np.linspace(max(var - 4, 0.1), var + 4, 100)  # 以最大似然估计的方差为中心，产生一组方差
p = normal_pdf(mean, var_range[:, None], data)  # 用正态分布的概率密度计算每个样本，每个方差所对应的概率密度
p = np.product(p, axis=1)  # 沿着P的第一轴求所有概率密度的乘积
plt.plot(var_range, p)
plt.axvline(var, 0, 1, c="r")
plt.show()
