# *.* coding=utf-8 *.*

import tensorflow as tf

matrix1 = tf.constant([[3., 3.]])
matrix2 = tf.constant([[2.], [2.]])


product = tf.matmul(matrix1,matrix2)

# 到目前为止，有三个节点（就是operation），两个是常量，一个是矩阵乘法

sess = tf.Session()
result = sess.run(product)

print(result)

sess.close()
