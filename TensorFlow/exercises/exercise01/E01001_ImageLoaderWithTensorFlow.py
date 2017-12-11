# _._encoding=utf-8_._

import tensorflow as tf
from utils import CV2Utils as cvtool
from utils import tfutils

with tf.Session() as sess:

    image_data = tfutils.tf_load_img("imgs/dog.jpg")

    cvtool.cvshow("this is a dog", image_data, img_swap=True)

    sess.close()
