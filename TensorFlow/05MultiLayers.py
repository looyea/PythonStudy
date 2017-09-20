# *.* coding=utf-8 *.*

import tensorflow as tf

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




