# _._encoding=utf-8_._

import numpy as np
import tensorflow as tf
from matplotlib import pyplot as plt
from matplotlib import cbook as cb


img = tf.gfile.FastGFile('./imgs/dog.jpg', 'rb').read()


sess = tf.InteractiveSession()

img_data_jpg = tf.image.decode_jpeg(img)  # 图像解码
img_data_jpg = tf.image.convert_image_dtype(img_data_jpg, dtype=tf.uint8)  # 改变图像数据的类型

plt.figure(1)  # 图像显示
plt.imshow(img_data_jpg.eval())
plt.show()
