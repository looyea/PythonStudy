# *.* coding=utf-8 *.*

import tensorflow as tf

with tf.Session() as sess:
    with tf.device("/gpu:0"): # 通过这种方式使用指定的设备进行计算
        matrix1 = tf.constant([[3., 3.]])
        matrix2 = tf.constant([[2.], [2.]])
        product = tf.matmul(matrix1, matrix2)
        result = sess.run(product)
        print(result)