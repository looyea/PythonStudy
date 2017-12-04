# -*- coding: utf-8 -*-

import tensorflow as tf

img_raw_data = tf.gfile.FastGFile('img/1.jpg', 'rb').read()

with tf.Session() as sess:
    img_data = tf.image.decode_jpeg(img_raw_data)
    # plt.imshow(img_data.eval())
    # plt.show()
    img_data = tf.image.rgb_to_grayscale(img_data)
    img_data = img_data.eval()

    print(img_data.reshape(784, 1).shape)
