# _._encoding=utf-8_._

import cv2
import sys
from PIL import Image


def CatchVideo(window_name, camera_idx):

    cap = cv2.VideoCapture(camera_idx)

    # 使用的人脸识别
    classifier = cv2.CascadeClassifier("/tools/anaconda3/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml")

    # 识别之后的边框颜色，RGB，
    color = (0, 255, 0)

    while cap.isOpened():
        # get a frame
        ret, frame = cap.read()
        if not ret:
            break

        # 获取灰度图像
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faceRects = classifier.detectMultiScale(grey, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32), maxSize=(256, 256))
        if len(faceRects) > 0:
            for faceRect in faceRects:
                x, y, w, h = faceRect
                cv2.rectangle(frame, (x-10, y-10), (x + w + 10, y + h + 10), color, 2)

        # show a frame
        cv2.imshow("capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    CatchVideo('视频流', 0)
