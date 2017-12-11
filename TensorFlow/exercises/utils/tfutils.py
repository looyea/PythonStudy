# _._encoding=utf-8_._

import tensorflow as tf


def tf_load_img(path_to_img, load_mod='rb', decode='jpeg'):

    with tf.Session() as sess:

        image_raw_data = tf.gfile.FastGFile(path_to_img, load_mod).read()

        image_data = None

        if decode == 'jpeg' or decode == 'jpg':
            image_data = tf.image.decode_jpeg(image_raw_data)

        if decode == 'bmp' or decode == 'BMP':
            image_data = tf.image.decode_bmp(image_raw_data)

        sess.close()
        return image_data

