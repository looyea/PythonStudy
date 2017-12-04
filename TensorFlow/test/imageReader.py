# _._encoding=utf-8_._


import cv2
import numpy as np

imgFilePath = 'img/dog.jpeg'

def readImg(imgFilePath):

    img = cv2.imread(imgFilePath, cv2.IMREAD_GRAYSCALE)




