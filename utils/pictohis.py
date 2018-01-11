# _._encoding=utf-8_._

import numpy as np

def imageToHistogram(image):
    x = image.shape[1]
    y = image.shape[0]
    print(x, y)
    listData = list(range(x))

    for i in range(0, x):
        listData[i] = 0
        for j in range(0, y):
            if image[j, i] < 255:
                listData[i] += 255
            else:
                listData[i] += 0

    for i in range(0, x):
        listData[i] /= y
    return listData