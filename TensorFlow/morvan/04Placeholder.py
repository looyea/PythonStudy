# *.* coding=utf-8 *.*

import tensorflow as tf

# 先声明一个变量了，不定义，具体的等到以后再说
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)

# 还可以规定结构,像下面这样的就是定义了一个2*2的张量了。
# input1 = tf.placeholder(tf.float32,[2,2])

# 输出也是可以定义的，就是一个乘法，当然这里只是一个临时的占位符
output = tf.multiply(input1, input2)

with tf.Session() as sess:
    # 注意这里面使用的都是张量，并且还都是浮点数啊
    # 其实不是这样的写，直接写2和5都可以，但是不严谨。
    print(sess.run(output,feed_dict={input1:[2.], input2: [5.]}))