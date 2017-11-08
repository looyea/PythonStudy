# *.* coding=utf-8 *.*

import tensorflow as tf

sess = tf.InteractiveSession()

x = tf.Variable([1.0, 2.0])
a = tf.constant([3.0, 3.0])

# 使用初始化进行run x
x.initializer.run()

# 通过这种方式直接持有图，而无需使用session，更加方便
sub = tf.subtract(x, a)

print(sub.eval())