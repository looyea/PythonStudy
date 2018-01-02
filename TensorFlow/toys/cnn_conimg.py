# _._encoding=utf-8_._

"""
目的是读取一个图片，然后设置一个卷积核，卷积该图片

然后看看图片的效果是啥样的。
"""

import tensorflow as tf
from matplotlib import pyplot as plt


def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1) # 变量的初始值为截断正太分布
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)



# 开启默认会话
sess = tf.InteractiveSession()

# 加载图像
img = tf.gfile.FastGFile('./img/dog.jpg', 'rb').read()


# 图像解码和图像数据类型转换
img_data_jpg = tf.image.decode_jpeg(img)  # 图像解码
img_data_jpg = tf.image.convert_image_dtype(img_data_jpg, dtype=tf.float32)  # 改变图像数据的类型

img_data_jpg = img_data_jpg.eval()

img_data_jpg = tf.image.resize_images(img_data_jpg, [300, 300], tf.image.ResizeMethod.AREA)
#
# W_conv1 = weight_variable([5, 5, 1, 32])  # 卷积是在每个5*5的patch中算出32个特征，分别是patch大小，输入通道数目，输出通道数目
# b_conv1 = bias_variable([32])
# h_conv1 = tf.nn.relu(tf.nn.conv2d(img_data_jpg, W_conv1, strides=[1, 1, 1, 1], padding='SAME') + b_conv1)
# h_pool1 = tf.nn.max_pool(h_conv1, ksize=[1, 2, 2, 1],
#                           strides=[1, 2, 2, 1], padding='SAME')
#
#
#
plt.figure(1)  # 图像显示
plt.imshow(img_data_jpg)
plt.show()



