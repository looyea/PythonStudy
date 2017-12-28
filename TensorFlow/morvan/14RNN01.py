# _._encoding=utf-8_._

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# this is data

mnist = input_data.read_data_sets('MNIST_data')

# hyper parameters
lr = 0.001  # 学习率
trainning_iters = 100000  # 学习步骤
batch_size = 128  # 批次量多大

n_inputs = 28  # MNIST 输入数据 28 × 28
n_steps = 28  # 时间步长
n_hidden_units = 128  # 隐藏层神经元
n_classes = 10  # MNIST分级（0 - 9个数字）

# tf graph input
x = tf.placeholder(tf.float32, [None, n_steps, n_inputs])
y = tf.placeholder(tf.float32, [None, n_classes])

# Define Weights
weights = {
    # (28, 128)
    'in': tf.Variable(tf.random_normal([n_inputs, n_hidden_units])),
    'out': tf.Variable(tf.random_normal(([n_hidden_units, n_classes])))
}

biases = {
    # (128,)
    'in': tf.Variable(tf.constant(0.1, shape=[n_hidden_units, ])),
    'out': tf.Variable(tf.constant(0.1, shape=[n_classes, ]))
}

## 定义RNN

def RNN(X, weights, biases):
    # hidden layer for input to cell, important
    # X结构（128批次，28行，28列） ==> (128*28, 28)
    X = tf.reshape(X, [-1, n_inputs])

    # ==> （128 × 28， 28）
    X_in = tf.matmul(X, weights['in']) + biases['in']
    # ==> （128 × 28 × 28）
    X_in = tf.reshape(X_in, [-1, n_steps, n_hidden_units])

    # cell
    lstm_cell = tf.nn.rnn_cell.BasicLSTMCell(n_hidden_units, forget_bias=1.0, state_is_tuple=True)
    # lstm cell contains 2 parts (c_state, m_state)
    _init_state = lstm_cell.zero_state(batch_size, dtype=tf.float32)

    outputs, states = tf.nn.dynamic_rnn(lstm_cell, X_in, initial_state=_init_state, time_major=False)


    # hidden layer for output as the final results
    # 用state 1是分线剧情的结果
    results = tf.matmul(states[1], weights['out']) + biases['out']

    # 或者用output解开，之后的效果一样
    # outputs = tf.unpack(tf.transpose(outputs, [1,0,2]))
    # results = tf.matmul(outputs[-1], weights['out']) + biases['out']
    # 就是看完所有内容之后总结的结果

    return results


pred = RNN(x, weights, biases)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=pred, logits=y))
train_op = tf.train.AdamOptimizer(lr).minimize(cost)

correct_pred = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    step = 0

    while step * batch_size < trainning_iters:
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        batch_xs = batch_xs.reshape([batch_size, n_steps, n_inputs])

        sess.run([train_op], feed_dict={
            x: batch_xs,
            y: batch_ys
        })

        if step % 20 == 0:
            print(sess.run(accuracy, feed_dict={
                x: batch_xs,
                y: batch_ys
            }))

        step += 1
