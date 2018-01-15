# _._encoding=utf-8_._


from utils.pictohis import *
from matplotlib import pyplot as plt
import cv2

if __name__ == "__main__":

    image = cv2.imread("./imgs/01.jpg")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    y = imageToHistogramNp(image)
    # y = imageToHistogram(image)
    x = range(len(y))

    plt.figure(1)
    plt.subplot(211)
    plt.plot(x, y)
    plt.subplot(212)
    plt.imshow(image)
    plt.show()
