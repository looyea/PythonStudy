#_._encoding=utf-8_._

import tensorflow as tf

# 定义了一个变量
state = tf.Variable(0,name='counter')

print(state.name)

# 定义了一个敞亮
one = tf.constant(1)

# 这里加法最后的结果，还是变量
newValue = tf.add(state, one)

# 将state = state + 1, 可以认为是定义了一个运算步骤
update = tf.assign(state, newValue)

# 如果定义变量了，就必须初始化
init = tf.initialize_all_variables()

# 还必须使用session.run进行激活
with tf.Session() as sess:
    sess.run(init)
    # 走三次循环
    for _ in range(3):
        # 每次+1
        sess.run(update)
        # 打印结果
        print(sess.run(state))