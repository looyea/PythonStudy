# _._encoding=utf-8_._

import cv2
import sys
import numpy as np

img = cv2.imread("./img/screenshot09.png")

pic_height, pic_width = img.shape[0], img.shape[1]

# 扫描范围
y_start = int(pic_height / 3)
y_end = y_start * 2
x_start = 0
x_end = pic_width

print(y_start, y_end, x_start, x_end)

# 按压时间比例系数
ratio_base = 2056
duration_ratio = ratio_base / pic_height

# 位置判定的相关内容
init_y, init_x = 0, 0
pos_min_x = x_end
pos_max_y = y_start
pos_det_x = 25
pos_det_y = 12

# 调试的时候，用来做中心位置判定的相关内容。主要看颜色了。
base_color = 73
base_list = list()


# 找到outline相关的内容
outline_color = None
init_y, init_x = 0, 0
min_x = 720
max_y = 0
init_found = False

for y in range(y_start, y_end):
    for x in range(x_start, x_end):
        # 找小人的位置
        if img[y, x, 0] == 73:
            if x <= pos_min_x:
                pos_max_y = y
                pos_min_x = x

for y in range(y_start, y_end):
    # 每一行起始的点
    check_point = img[y, 0]
    for x in range(x_start, x_end):
        if img[y, x, 0] != check_point[0]:
            outline_color = img[y, x]
            init_y, init_x = y, x
            init_found = True
            break
    if init_found:
        break

# y 最大物体172，一半是81，取闭区间是81， 从下一行开始扫描
for y in range(init_y + 1, init_y + 82):
    check_point = img[y, 0]
    # 同样扫描X从0，到初始点
    for x in range(0, init_x + 1):
        # 如果颜色点不同, 并且在临近色域内
        if img[y, x, 0] != check_point[0] and np.sqrt(np.sum(np.square(img[y, x] - outline_color))) <= 3.0:
            # 找最小
            if x < min_x:
                img[y, x] = [255, 0, 0]
                min_x = x
                max_y = y
                continue

img[max_y, min_x] = 255

img[pos_max_y + pos_det_y, pos_min_x + pos_det_x] = 255


cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


