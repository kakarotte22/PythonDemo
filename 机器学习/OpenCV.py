import cv2
#1、从窗口显示一副图片
# cv2.namedWindow('winName', cv2.WINDOW_NORMAL)     #参数为：窗口名称，可以手动调节窗口大小
# img = cv2.imread('myPIC.jpg', 1)    #1：原色图片；0：黑白图片
# cv2.imshow('winName', img)   #显示图片
# cv2.waitKey(0)
# cv2.destroyAllWindows()  #销毁创建的对象
# #2、保存图片：OpenCV可将图片转换为PGM格式
# cv2.imwrite('pic2PGM.pgm', img)
# #3、在matplotlib中显示图片
# from matplotlib import pyplot as plt
# img = cv2.imread('pic2PGM.pgm', 0)
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.xticks([]), plt.yticks([])
# plt.show()
#4、绘制直线和矩形
from numpy import *
img = zeros((512, 512, 3))
#起点：（0,0），终点：（511,511），颜色：（0,255,255），像素：2
cv2.line(img, (0, 0), (511, 511), (0, 255, 255), 2)
#左上角：（150,150）；右下角：（350,350）；颜色：（255,255,0）BGR；像素：2
cv2.rectangle(img, (150, 150), (350, 510), (255, 255, 0), 2)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#5、绘制圆形和椭圆形：
# cv2.circle(img, center, radius, color, thickness=None, lineType=None, shift=None)
# cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color, thickness=None, lineType=None, shift=None)
#6、绘制多边形
# cv2.polylines(img, pts, isClosed, color, thickness=None, lineType=None, shift=None)
#7、写入文字
# font = cv2.FONT_HERSHEY_COMPLEX  #字体
# cv2.putText(img, text, org, fontFace, fontScale, color, thickness=None, lineType=None, bottomLeftOrigin=None)