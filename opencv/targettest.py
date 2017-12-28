# _._encoding=utf-8_._

# 用于模型的单张图像分类操作
import os

os.environ['GLOG_minloglevel'] = '2'  # 将caffe的输出log信息不显示，必须放到import caffe前
import caffe  # caffe 模块
from caffe.proto import caffe_pb2
from google.protobuf import text_format
import numpy as np
import cv2
import matplotlib.pyplot as plt
import time
import skimage.io

global num
num = 0


def detect(image1, net):
    # 传进来的image1的dtype为uint8
    # print image1.shape
    # print image1.dtype
    # print image1.size

    # image = np.array(image1, dtype=np.float32)
    # image = caffe.io.resize_image(image1, (480, 640))
    image = skimage.img_as_float(image1).astype(np.float32)
    # image = caffe.io.resize_image(image2, (300, 300))

    # skimage.io.imsave("photo.png", image)
    # cv2.imwrite("photo.png", image)
    # image = caffe.io.load_image(caffe_root + 'examples/images/bird.jpg')
    # 以下方式读取的imaged的dtype为float32
    # image = caffe.io.load_image(caffe_root + 'photo.png')
    # image = caffe.io.load_image(image1)

    # 改变dtype
    # image.dtype = 'float32'
    # print 'mode:'+image.mode
    # print image.shape
    # print image.dtype
    # print image.size

    # plt.imshow(image)

    # * Run the net and examine the top_k results
    # In[5]:
    global num
    num += 1
    print('image num:' + str(num))

    transformed_image = transformer.preprocess('data', image)
    net.blobs['data'].data[...] = transformed_image

    time_start = time.time()
    # Forward pass.
    net.forward()

    time_end = time.time()
    print('time:' + str(time_end - time_start) + ' s')

    loc = net.blobs['bbox-list'].data[0]
    print(loc)
    # 查看了结构文件发现在CAFFE一开始图像输入的时候就已经将图片缩小了，宽度1248高度384
    # 然后我们在net.blobs['bbox-list'].data得到的是侦测到的目标座标，但是是相对于1248*384的
    # 所以我们要把座标转换回相对原大小的位置，下面im.shape是保存在原尺寸的宽高，
    for l in range(len(loc)):
        xmin = int(loc[l][0] * image.shape[1] / 1248)
        ymin = int(loc[l][1] * image.shape[0] / 384)
        xmax = int(loc[l][2] * image.shape[1] / 1248)
        ymax = int(loc[l][3] * image.shape[0] / 384)
        # 在该座标位置画一个方框
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (55 / 255.0, 255 / 255.0, 155 / 255.0), 2)
        # 显示结果

    # plt.imshow(image, 'brg')
    # plt.show()
    cv2.imshow('img', image)


def show_info(cam):
    print('POS_FRAMES:' + str(cam.get(1)))
    print('FRAME_COUNT:' + str(cam.get(7)))
    print('FORMAT:' + str(cam.get(8)))
    print('MODE:' + str(cam.get(9)))
    print('SATURATION:' + str(cam.get(12)))
    print('FPS:' + str(cam.get(5)))


# CPU或GPU模型转换
caffe.set_mode_gpu()
# caffe.set_mode_cpu()
# caffe.set_device(0)

caffe_root = '/var/smb/work/mycode/'
# 网络参数（权重）文件
caffemodel = caffe_root + 'module/detectnet/snapshot_iter_2391.caffemodel'
# 网络实施结构配置文件
deploy = caffe_root + 'module/detectnet/deploy.prototxt'

img_root = caffe_root + 'data/'

# 网络实施分类
net = caffe.Net(deploy,  # 定义模型结构
                caffemodel,  # 包含了模型的训练权值
                caffe.TEST)  # 使用测试模式(不执行dropout)

# 加载ImageNet图像均值 (随着Caffe一起发布的)
print(os.environ['PYTHONPATH'])
# mu = np.load(os.environ['PYTHONPATH'] + '/caffe/imagenet/ilsvrc_2012_mean.npy')
# mu = mu.mean(1).mean(1)  # 对所有像素值取平均以此获取BGR的均值像素值

# 图像预处理
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2, 0, 1))
# transformer.set_mean('data', mu)
transformer.set_raw_scale('data', 255)
transformer.set_channel_swap('data', (2, 1, 0))

# 处理图像
cam = cv2.VideoCapture(0)
if cam.isOpened():
    cam.set(3, 400)
    cam.set(4, 300)
    cam.set(5, 3)
    time.sleep(6)
    cam.set(15, -8.0)
    size = (int(cam.get(3)), int(cam.get(4)))
    print('size:', size)

cv2.namedWindow('img', cv2.WINDOW_NORMAL)

# cnt=2
# while cnt:
#     cnt -= 1
while cam.isOpened():
    ret, img = cam.read()
    if ret:
        # show_info(cam)
        detect(img, net)

    if 0xFF == ord('q') & cv2.waitKey(5) == 27:
        break
        # time.sleep(0.033)
cam.release()
cv2.destroyAllWindows()