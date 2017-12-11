# _._encoding=utf-8_._

"""
展示了图像的四种改变大小的方法。
"""

import tensorflow as tf
from utils import CV2Utils as cvtool
from utils import tfutils

new_size = [300, 300]

with tf.Session() as sess:

    image_data = tfutils.tf_load_img("imgs/dog.jpg")

    image_data_area_resized = tf.image.resize_images(image_data, new_size, tf.image.ResizeMethod.AREA)

    cvtool.cvshow("this is a dog", image_data_area_resized)

    image_data_bilinear_resized = tf.image.resize_images(image_data, new_size, tf.image.ResizeMethod.BILINEAR)

    cvtool.cvshow("this is a dog", image_data_bilinear_resized)

    image_data_nearest_neighbor_resized = \
        tf.image.resize_images(image_data, new_size, tf.image.ResizeMethod.NEAREST_NEIGHBOR)

    cvtool.cvshow("this is a dog", image_data_nearest_neighbor_resized)

    image_data_bicubic_resized = tf.image.resize_images(image_data, new_size, tf.image.ResizeMethod.BICUBIC)

    cvtool.cvshow("this is a dog", image_data_bicubic_resized)

    sess.close()
