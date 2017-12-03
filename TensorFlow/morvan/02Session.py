# _._encoding=utf-8_._
import tensorflow as tf

matrix1 = tf.constant([[3,3]])
matrix2 = tf.constant([[2],[2]])

product = tf.matmul(matrix1, matrix2)

# 运行形式一
# session = tf.Session()
# result = session.run(product)
# print(result)
# session.close()

# 运行形式二
with tf.Session() as sess:
    result2 = sess.run(product)
    print(result2)
