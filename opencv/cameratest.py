# _._encoding=utf-8_._

import cv2
import numpy
import matplotlib.pyplot as plot


# 使用的自带摄像头开启，0 一般是内置摄像头，例如笔记本的
cap = cv2.VideoCapture(0)


# 不停的读取摄像头中的图像, 知道检测到q键按下，退出，使用的是64位按键检测
while True:
    # get a frame
    ret, frame = cap.read()
    # show a frame
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头
cap.release()

# 销毁所有的窗口
cv2.destroyAllWindows()
