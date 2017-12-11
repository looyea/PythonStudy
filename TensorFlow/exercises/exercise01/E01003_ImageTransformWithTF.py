# _._encoding=utf-8_._

"""
展示了如何改变图像大小的办法
"""

import tensorflow as tf
from utils import CV2Utils as cvtool
from utils import tfutils


with tf.Session() as sess:
    image_data = tfutils.tf_load_img("imgs/dog.jpg")

    cvtool.cvshow("original now ", image_data)

    cropped_image = tf.image.crop_to_bounding_box(image_data, 20, 20, 256, 256)

    cvtool.cvshow("cropped dog", cropped_image)

    left_flipped_image = tf.image.flip_left_right(image_data)

    cvtool.cvshow("left right dog", left_flipped_image)

    updown_flipped_image = tf.image.flip_up_down(image_data)

    cvtool.cvshow("updown dog", updown_flipped_image)

