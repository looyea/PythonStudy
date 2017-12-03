# _._encoding=utf-8_._

# remember to define the same dtype and shape when restore
import tensorflow as tf

W = tf.Variable([[1, 2, 3], [3, 4, 5]],dtype=tf.float32, name='weights')

b = tf.Variable([[1, 2, 3]], dtype=tf.float32, name='bias')

init = tf.global_variables_initializer()

saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(init)

    save_path = saver.save(sess, "my_net/save_net.ckpt")

    print("save to path my_net")
