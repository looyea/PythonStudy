# _._encoding=utf-8_._

import cv2
import tensorflow
import numpy as np
from matplotlib import pyplot as plt


img_ref_bgr = cv2.imread('./img/2.jpg')

cv2.imshow('org', img_ref_bgr)
cv2.waitKeyEx(0)
cv2.destroyWindow('org')

img_ref_gray = (cv2.cvtColor(img_ref_bgr, cv2.COLOR_BGR2GRAY))/255.0


cv2.imshow('img', img_ref_gray)
cv2.waitKeyEx(0)
cv2.destroyWindow('img')
