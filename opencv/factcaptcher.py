# _._encoding=utf-8_._

"""
目标是通过按下Q键捕获当前正脸照相

这里是数据采集的方式去进行的

当按下Q键之后：
    1. 采集当前图像
    2. 将图像转换为灰度图像
    3. 将图像保存

注意图像大小是64 × 64

关于图片相似度的算法，参考了这里
http://www.jb51.net/article/83315.htm

"""

import cv2
import os
import numpy as np

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
        image = image[frame_y + 2: frame_y + frame_w, frame_x: frame_x + frame_w]
        image = relight(image)

        cv2.imshow("cut", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        # 需要使用截取范围对图像进行裁剪这样才行
        cv2.imwrite(out_dir + '/myface.jpg', image)

        break

# 释放摄像头
cap.release()

# 销毁所有的窗口
cv2.destroyAllWindows()

def Hamming_distance(hash1,hash2):
 num = 0
 for index in range(len(hash1)):
  if hash1[index] != hash2[index]:
   num += 1
 return num

def classify_pHash(image1,image2):
 image1 = cv2.resize(image1, (32, 32))
 image2 = cv2.resize(image2, (32, 32))
 gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
 gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
 # 将灰度图转为浮点型，再进行dct变换
 dct1 = cv2.dct(np.float32(gray1))
 dct2 = cv2.dct(np.float32(gray2))
 # 取左上角的8*8，这些代表图片的最低频率
 # 这个操作等价于c++中利用opencv实现的掩码操作
 # 在python中进行掩码操作，可以直接这样取出图像矩阵的某一部分
 dct1_roi = dct1[0:8, 0:8]
 dct2_roi = dct2[0:8, 0:8]
 hash1 = getHash(dct1_roi)
 hash2 = getHash(dct2_roi)
 return Hamming_distance(hash1, hash2)


# 输入灰度图，返回hash
def getHash(image):
    avreage = np.mean(image)
    hash = []
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i, j] > avreage:
                hash.append(1)
            else:
                hash.append(0)
    return hash

img1 = cv2.imread('faces/myface.jpg')
cv2.imshow('img1', img1)
img2 = cv2.imread('my_faces/2.jpg')
cv2.imshow('img2', img2)
degree = classify_pHash(img1, img2)
print('相似度：', (64 - degree) / 64.0)
