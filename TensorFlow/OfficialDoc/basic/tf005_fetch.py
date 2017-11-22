# *.* coding=utf-8 *.*

import tensorflow as tf

input1 = tf.constant(3.0)
input2 = tf.constant(2.0)
input3 = tf.constant(5.0)
intermed = tf.add(input2, input3)
mul = tf.multiply(input1, intermed)

with tf.Session() as sess:
    result = sess.run([mul, intermed]) # 这里走计算图定义的顺序，而不是打印顺序
    print(result)
    print(mul)
    print(intermed)
