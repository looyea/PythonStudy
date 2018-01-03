# _._encoding=utf-8_._
"""
平均脸的玩法，
只是做了简单的算数平均脸
如果需要可以考虑提取特征

先得综合矩阵的算数平均值

记录特征，然后每个矩阵 - 平均矩阵得到离散差

然后这个离散度×自身的转置，进而求出其他的情况

"""

import cv2
import os
import numpy as np
import sys

input_dir = './other_faces'
size = 64

avg_face = np.matrix(np.zeros([64, 64]))

print("initialized avg_face ", avg_face)

idx_face = 0
max_num_faces = 5000
avg_tuner = 210


# 处理过亮或者过暗的情况
def relight(img, alpha=1, bias=0):
    w = img.shape[1]
    h = img.shape[0]

    for i in range(0, w):
        for j in range(0, h):
            for c in range(3):
                tmp = int(img[j, i, c] * alpha + bias)
                if tmp > 255:
                    tmp = 255
                elif tmp < 0:
                    tmp = 0
                img[j, i, c] = tmp
    return img


for (path, dirnames, filenames) in os.walk(input_dir):
    for filename in filenames:

        idx_face += 1
        img_path = path+'/'+filename
        # 从文件读取图片
        img = cv2.imread(img_path)
        # img = relight(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        avg_face = img + avg_face

        if idx_face == max_num_faces:
            break
            # sys.exit(0)

avg_face = avg_face / max_num_faces / avg_tuner

cv2.imshow("avg face", avg_face)
cv2.waitKey(0)
cv2.destroyAllWindows()

