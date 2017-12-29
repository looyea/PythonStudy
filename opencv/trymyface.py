# _._encoding=utf-8_._

import cv2
import dlib
import os
import sys
import random

output_dir = '/home/looyea/faces/looyea'
size = 64

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

# 改变图片亮度与对比度
def relight(img, light=1, bias=0):
    w = img.shape[1]
    h = img.shape[0]

    for i in range(0, w):
        for j in range(0, h):
            for c in range(3):
                temp = int(img[j, i, c]*light + bias)
                if temp > 255:
                    temp = 255
                elif temp < 0:
                    temp = 0
                img[j, i, c] = temp

    return img

detector = dlib.get_frontal_face_detector()

camera = cv2.VideoCapture()

index = 1

while True:
    ret, img = camera.read()
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # show a frame
    cv2.imshow("capture", img)
    dets = detector(gray_img, 1)

    if cv2.waitKey(1) & 0xFF == ord('c'):
        for i, d in enumerate(dets):
            x1 = d.top() if d.top() > 0 else 0
            y1 = d.bottom() if d.bottom() > 0 else 0
            x2 = d.left() if d.left() > 0 else 0
            y2 = d.right() if d.right() > 0 else 0

            face = img[x1:y1, x2:y2]
            # 调整图片的对比度与亮度， 对比度与亮度值都取随机数，这样能增加样本的多样性
            face = relight(face, random.uniform(0.5, 1.5), random.randint(-50, 50))

            face = cv2.resize(face, (size, size))

            cv2.imshow('image', face)

            cv2.imwrite(output_dir + '/' + str(index) + '.jpg', face)

            index += 1
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break
