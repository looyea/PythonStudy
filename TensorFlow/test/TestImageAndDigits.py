# _._encoding=utf-8_._

import tensorflow as tf
import cv2
import numpy as np
from sys import path

from tensorflow.examples.tutorials.mnist import input_data



mnist = input_data.read_data_sets("MNIST_data", one_hot=True)


def compute_accuracy(v_xs, v_ys):
    global prediction
    y_pre = sess.run(prediction, feed_dict={xs: v_xs, keep_prob: 1})
    correct_prediction = tf.equal(tf.argmax(y_pre,1), tf.argmax(v_ys,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys, keep_prob: 1})
    return result

# 根据形状创建权重
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

# 根据输入创建偏置量
def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

def conv2d(x,W):
    # stride, 步长, 开始结束必须是1, 中间两个分别是xy方向的步长
    return tf.nn.conv2d(x, W, strides=[1,1,1,1], padding='SAME')

def max_pool_2x2(x):
    # 这里使用2个步长移动一下, 保证压缩图片长宽
    # stride, 步长, 开始结束必须是1, 中间两个分别是xy方向的步长
    return tf.nn.max_pool(x, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')

xs = tf.placeholder(tf.float32, [None, 784]) # 28 * 28
ys = tf.placeholder(tf.float32, [None, 10])
keep_prob = tf.placeholder(tf.float32)

# x 数据是28 * 28, 所以中间的x,y是28 和28
# 维度暂时不管, 所以是-1, 渠道是1, 是因为只有黑白
x_image = tf.reshape(xs, [-1, 28,28, 1])

# print(x_image.shape) # [n_sample, 28, 28,1 ]

## conv1 layer ##
## 5,5 表示卷积核大小5*5, 输入尺寸是1, 输出的是32
W_conv1 = weight_variable([5,5,1,32])

# 偏置量因为输出的weight是32, 所以这里就是32啊
b_conv1 = bias_variable([32])

# 定义一个隐形层节点, 通过relu函数处理
# output size = 28 * 28 * 32
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)

# 定义隐形层的pooling
# output size = 14 * 14 * 32, 因为步长是2, 做了形状变化
h_pool1 = max_pool_2x2(h_conv1)

## conv2 layer ##
## 图片变高,变厚了, 所以这里就不一样了, 因为padding的是2, 所以这里翻倍!
W_conv2 = weight_variable([5,5,32,64])
b_conv2 = bias_variable([64])
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2) ## 7 * 7 * 64

## func1 layer ##

W_func1 = weight_variable([7*7*64, 1024])
b_func1 = bias_variable([1024])
h_pool2_flat = tf.reshape(h_pool2, [-1,7*7*64]) # [n_samples, 7, 7, 64] -> [ n_sample, 7*7*64]
h_func1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_func1) + b_func1)
# dropout processing
h_fc1_drop = tf.nn.dropout(h_func1, keep_prob)

## func2 layer ##
W_func2 = weight_variable([1024, 10])
b_func2 = bias_variable([10])
prediction = tf.nn.softmax(tf.matmul(h_fc1_drop, W_func2) + b_func2)

## loss funcitn
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction),
reduction_indices=[1])) # loss


## 梯度下降求最小交叉熵验证
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

sess = tf.Session()

sess.run(tf.global_variables_initializer())

for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={xs: batch_xs, ys: batch_ys, keep_prob: 0.5})
    if i % 50 == 0:
        print(compute_accuracy(
            mnist.test.images[:1000], mnist.test.labels[:1000]))

# mnist_data_set = extract_mnist.MnistDataSet('../../data/')
# x_img , y  = mnist_data_set.next_train_batch(1)
im = cv2.imread('img/1.jpg', cv2.IMREAD_GRAYSCALE).astype(np.float32)
im = cv2.resize(im, (28, 28), interpolation=cv2.INTER_CUBIC)
# 图片预处理
# img_gray = cv2.cvtColor(im , cv2.COLOR_BGR2GRAY).astype(np.float32)
# 数据从0~255转为-0.5~0.5
img_gray = (im - (255 / 2.0)) / 255

# cv2.imshow('out',img_gray)
# cv2.waitKey(0)

x_img = np.reshape(img_gray, [-1, 784])

print(x_img)

output = sess.run(prediction, feed_dict={xs: x_img, ys: [0,1,0,0,0,0,0,0,0,0]})
print('the y_con :   ', '\n', output)
print('the predict is : ', np.argmax(output))

# 关闭会话
sess.close()