# _._ encoding=utf-8 _._
'''
针对上次的内容进行可视化
'''

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 添加一个层
def add_layer(inputs, in_size, out_size, activation_function = None):

    # 尽量使用随机变量，在使用初始位置比较好
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))

    # 偏置量
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)

    # 预测的值，还没有被激活
    Wx_plus_b = tf.matmul(inputs, Weights) + biases

    # 当没有激活函数的时候，这里就是当他是线性的
    if activation_function is None:
        outputs = Wx_plus_b

    # 不是空的时候，就使用具体的激活函数进行处理
    else:
        # 然后用激活函数来看，是否靠谱，说白了，激活函数就是一个检验的
        outputs = activation_function(Wx_plus_b)

    return outputs


# 定义X数据
x_data = np.linspace(-1,1,300)[:,np.newaxis]

# 定义噪音内容
noise = np.random.normal(0,0.05,x_data.shape)

# 使用噪音使得数据更真是
y_data = np.square(x_data) - 0.5 + noise

xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])

# 需要定义，输入，隐藏，输出

# 定义隐藏层
layer_hidden = add_layer(xs, 1, 10, activation_function=tf.nn.relu)

# 就是输出层
prediction = add_layer(layer_hidden, 10, 1, activation_function=None)

# 定义损失函数
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))

# 定义练习的部分
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

# 初始化变量
init = tf.global_variables_initializer()

sess = tf.Session()

sess.run(init)

# 可视化的内容
fig = plt.figure()
# 连续行画图，就需要这个
ax = fig.add_subplot(1,1,1)
ax.scatter(x_data, y_data)
plt.ion() # 连续的内容显示，不需要暂停程序
plt.show() # 老版本这里就是plt.show(block=False)

for i in range(1001):
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    if i % 50 == 0:
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        prediction_value = sess.run(prediction, feed_dict={xs:x_data, ys:y_data})
        lines = ax.plot(x_data, prediction_value, 'r-', lw=5)
        plt.pause(0.1)

plt.pause(5)
