# _._ encoding=utf-8 _._


import tensorflow as tf
import numpy as np

# 添加一个层
def add_layer(inputs, in_size, out_size, activation_function = None):
    with tf.name_scope('layer'):
        with tf.name_scope('weights'):
            # 尽量使用随机变量，在使用初始位置比较好
            Weights = tf.Variable(tf.random_normal([in_size, out_size]), name='w')

        with tf.name_scope('biases'):
            # 偏置量
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, name='b')

        with tf.name_scope('Wx_pls_b'):
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

with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32, [None, 1], name='x_input')
    ys = tf.placeholder(tf.float32, [None, 1], name='y_input')

# 需要定义，输入，隐藏，输出

# 定义隐藏层
layer_hidden = add_layer(xs, 1, 10, activation_function=tf.nn.relu)

# 就是输出层
prediction = add_layer(layer_hidden, 10, 1, activation_function=None)

with tf.name_scope('loss'):
    # 定义损失函数
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))

with tf.name_scope('train'):
    # 定义练习的部分
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

sess = tf.Session()

writer = tf.summary.FileWriter("/home/appadmin/", tf.get_default_graph())

sess.run(tf.global_variables_initializer())

writer.close()
