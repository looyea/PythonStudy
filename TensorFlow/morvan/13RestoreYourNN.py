
import tensorflow as tf
import numpy as np

W = tf.Variable(np.arange(6).reshape((2, 3)), dtype=tf.float32, name="weights")
# 这里注意, 保存的时候和读取的时候数据类型不仅一样, 而且空间结构也必须相同. 不然报错
b = tf.Variable(np.arange(3).reshape((1, 3)), dtype=tf.float32, name="bias")


saver = tf.train.Saver()
with tf.Session() as sess:
    # 这个路径一定注意! 差一点都不行,不知道为什么保存的时候可以直接用相对路径,读取的时候就不行!
    saver.restore(sess, "D:/pywork/PythonStudy/TensorFlow/morvan//my_net/save_net.ckpt")
    print("weights ", sess.run(W))
    print("Bias ", sess.run(b))
