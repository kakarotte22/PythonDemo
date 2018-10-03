#可以用几种特征来表示人脸的大致结构：眼睛、鼻子、前额、额骨和嘴，满足这些结构特征我们就认为这是一张人脸，为了提高运算速度，
#我们选择排除图片中不包含人脸的位置，称这个过程为级联过程。，但人脸的特征远比这几个复杂的多，OpenCV里常用的人脸特征有Haar特征和LBP特征。
#如果使用Haar特征，就需要使用Haar特征级联表作为训练集，在OpenCV根目录/sourse/data/  文件夹下
from numpy import *
import cv2
face_cascade = cv2.CascadeClassifier(r'C:\Users\Administrator\Desktop\opencv-3.4.1\opencv-3.4.1\data\haarcascades\haarcascade_frontalface_alt_tree.xml')
img = cv2.imread('testPic.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   #转换成gray，opencv使用灰度图像处理
faces = face_cascade.detectMultiScale(gray, 1.1, 0)
#detectMultiScale(需要识别的图片, 尺寸缩小比例, 3表示至少被检测4次才算真的目标)
# print(faces, type(faces))
for (x, y, w, h) in faces:   #绘制人脸边框
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('testPic2.head.jpg', img)
print('end')