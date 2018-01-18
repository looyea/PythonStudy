# _._encoding=utf-8_._

import numpy as np

def imageToHistogram(image):
    """
    基本方法做直方图，没有最低Gap处理
    :param image:
    :return:
    """
    x = image.shape[1]
    y = image.shape[0]
    print(x, y)
    listData = list(range(x))

    for i in range(0, x):
        listData[i] = 0
        for j in range(0, y):
           listData[i] += image[j, i]

    for i in range(0, x):
        listData[i] /= y

    _max = max(listData)
    _min = min(listData)

    for i in range(0, x):
        listData[i] = _max - listData[i]


    return listData


def imageToHistogramNp(image):
    """
    这个就是针对图像的横轴，每个横轴上的x，计算纵轴的y的累加
    然后取累加平均值，方便处理。
    为了保证图片中的文字可以被良好的切割开，做了底线处理。
    按照最大最小值之间gap的10%作为标准，低于10%的值，都给0
    这样，就可能通过0，清楚的区分出来各个数字（文字）正确的
    位置了。
    :param image: 传入的图像
    :return:
    """
    x = image.shape[1]
    y = image.shape[0]
    print(x, y)

    listData = np.mean(image, axis=0)

    _max = max(listData)
    _min = min(listData)

    gap = (_max - _min) * 0.10

    listData = _max - listData

    for i in range(x):
        if listData[i] < gap:
            listData[i] = 0

    return listData
