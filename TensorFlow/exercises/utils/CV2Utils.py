# _._encoding=utf-8_._

import cv2

# use cv2 to show picture data
def cvshow(show_title, show_img=None, show_time=5000, img_swap=False):
    if show_img is None:
        return
    # 获取矩阵信息
    np = show_img.eval()
    # 获取行数列数
    row, col = len(np), len(np[1])

    if img_swap:
        # 两重循环遍历
        for i in range(row):
            for j in range(col):
                # 交换数值
                np[i][j][0], np[i][j][2] = np[i][j][2], np[i][j][0]

    # 显示图片
    cv2.imshow(show_title, np)
    cv2.waitKeyEx(show_time)
    cv2.destroyWindow(show_title)
