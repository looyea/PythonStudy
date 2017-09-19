# _._encoding=utf-8_._
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 创建数据
x_data = np.random.rand(100).astype(np.float32)

# 预测创建y值范围, 当然Y值可以随便给，但是这样做没有意义啊
# 因为如果随机给的话，很可能是个离散的点, 最后得到的也是没用的结果
# 也就是Garbage in Garbage Out！
# 所以这里最终的目的就是验证，通过TF训练结果是什么样子的，
# 会得到什么样的权重和偏差的输出！
y_data = x_data * 0.1 + 0.3

# 创建tensorflow结构 开始

# 权重，可能是矩阵
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
# 偏执函数
Biases = tf.Variable(tf.zeros([1]))

# 定义神经节点也就是预测值
y = Weights * x_data + Biases
# 定义损失函数
loss = tf.reduce_mean(tf.square(y - y_data))

# 定义优化器的使用方式，参数是学习效率，一般＜1，这里给0.5
optimizer = tf.train.GradientDescentOptimizer(0.5)
# 训练损失函数相关的内容, 目标就是最小化误差
train = optimizer.minimize(loss)
# 初始化所有的变量
init = tf.initialize_all_variables()

# 以上就是神经网络主要的实现过程

# 创建tensorflow结构 结束


# 以上定义好了结构，开始进行激活和初始化
session =tf.Session()
# 开始运行神经网络
session.run(init) # 激活还是很重要的步骤。

for step in range(2001):
    session.run(train)   # 说明训练的是谁？
    if step % 20 == 0:
        print(step, session.run(Weights), session.run(Biases)) # 输出当前的权重和偏差函数是多少


# 201次训练结果, 可以说是非常接近最初给的值了！
'''
0 [-0.33321208] [ 0.73324233]
20 [-0.05004987] [ 0.37986964]
40 [ 0.05647305] [ 0.32316884]
60 [ 0.08737357] [ 0.30672091]
80 [ 0.09633729] [ 0.30194962]
100 [ 0.09893751] [ 0.30056557]
120 [ 0.09969179] [ 0.30016407]
140 [ 0.09991059] [ 0.30004761]
160 [ 0.09997407] [ 0.30001381]
180 [ 0.09999246] [ 0.30000404]
200 [ 0.09999781] [ 0.30000117]
'''