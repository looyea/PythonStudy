# *.* coding=utf-8 *.*

import tensorflow as tf

# Variants playing~~

state = tf.Variable(0, name='counter')

# 实现了自加
one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)

init_op = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init_op)
    print(sess.run(state))

    for _ in range(3):
        sess.run(update)
        print(sess.run(state))