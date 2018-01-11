# _._encoding=utf-8_._

"""
专门用来生成指定文字标签的图片
长短可调

最后的目的是，将生成的图片，转化成直方图，根据直方图的高点和低谷
找稀疏范围，按照范围截取图片指定的区域
最后将区域的内容，转换成相关的数据，识别成图片来进行处理。
"""

import cv2
import numpy as np
from utils.timeutils import *
from matplotlib import pyplot as plt
import math


def gen_pic_with_text(content):
    if content is None:
        print("String to put shuold not be none!")
    # 设定画布大小, 设定背景色
    canvas = np.zeros((80, 250))
    canvas.fill(255)

    # 印刷文字
    cv2.putText(canvas, content, (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, 0, 2)

    # 预览图片信息
    # cv2.imshow("img", canvas)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return canvas


