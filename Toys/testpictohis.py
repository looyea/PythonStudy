# _._encoding=utf-8_._
"""
直方图法进行图像分割
以后可以通过CNN卷积网络，将图片中背景色的点进行卷积
最后除掉背景色后，进行深色累积，最终只保留包含文字特征的矩阵
最后通过矩阵拆解、Padding，传递CNN网络进行单个的文字识别
非常好用！！
"""

from utils.timeutils import *
from utils.LabelPicGenerator import *
from utils.pictohis import *
from matplotlib import pyplot as plt

if __name__ == "__main__":
    time_str = gen_time_string()
    image = gen_pic_with_text(time_str)
    y = imageToHistogram(image)
    x = range(len(y))

    plt.figure(1)
    plt.subplot(211)
    plt.plot(x, y)
    plt.subplot(212)
    plt.imshow(image)
    plt.show()
