# _._encoding=utf-8_._

"""
目标是通过按下Q键捕获当前正脸照相

这里是数据采集的方式去进行的

当按下Q键之后：
    1. 采集当前图像
    2. 将图像转换为灰度图像
    3. 将图像保存

注意图像大小是64 × 64
"""

import cv2
import os
import random

out_dir = './faces'
if not os.path.exists(out_dir):
    os.makedirs(out_dir)


# 改变亮度与对比度
def relight(img, alpha=1, bias=0):
    w = img.shape[1]
    h = img.shape[0]

    for i in range(0, w):
        for j in range(0, h):
            for c in range(3):
                tmp = int(img[j, i, c]*alpha + bias)
                if tmp > 255:
                    tmp = 255
                elif tmp < 0:
                    tmp = 0
                img[j, i, c] = tmp
    return img


# 获取分类器
# classifier = cv2.CascadeClassifier("/tools/anaconda3/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml")

# 使用的自带摄像头开启，0 一般是内置摄像头，例如笔记本的
cap = cv2.VideoCapture(0)


# 不停的读取摄像头中的图像, 知道检测到q键按下，退出，使用的是64位按键检测
while True:
    # get a image
    ret, image = cap.read()

    # 设置相框位置和大小，这里是相对的，取画面长边的十分之一
    image_shape = image.shape
    img_h, img_w = image_shape[0], image_shape[1]
    scale = 4   # 图像缩放比例
    frame_w = int(img_w / scale)
    frame_h = frame_w
    frame_x = int((img_w - frame_w) / 2) - 2
    frame_y = int((img_h - frame_w) / 2) - 2

    # show a frame
    cv2.rectangle(image, (frame_x, frame_y), (frame_x + frame_w + 4, frame_y + frame_w + 4),
                  color=(0, 255, 0), thickness=2)
    cv2.imshow("capture", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        image = relight(image)
        # 需要使用截取范围对图像进行裁剪这样才行
        cv2.imwrite(out_dir + '/myface.jpg', image)
        break

# 释放摄像头
cap.release()

# 销毁所有的窗口
cv2.destroyAllWindows()
