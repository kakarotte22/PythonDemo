import numpy as np
from numpy import *
# #a1,a2,a3分别表示在直角坐标系中的坐标，现将原坐标系变换成a1,a2为基地的坐标系中，求变换后的a3在哪（直角坐标系）
# a1 = [3, 1]
# a2 = [1, 3]
# a3 = [1, 2]
# a = mat([a1, a2])
# print(a3 * a)
# print(a)
# #需要变换的向量或向量组 * 基地向量组 = 变换后的向量位置，因此矩阵乘法是一种‘变换’
# #线性变换要求必须通过基地向量构成的坐标系原点，而线性变换只要是原向量发生旋转、伸缩，故比如存在一个向量，只发生了伸缩变换，
# # 这个向量就是特征向量，故A *v = r * v，（v是A的特征向量，r是对应的特征值）
# print('*' * 30)
# A =[[8, 1, 6], [3, 5, 7], [4, 9, 2]]
# evals, evecs = linalg.eig(A)
# print(evals)
# print(evecs)
# print('*' * 30)
# print(np.indices((3, 3)))   #得到形状为3 * 3的矩阵的 行索引矩阵，和列索引矩阵，
# print('*' * 30)


import matplotlib.pyplot as plt
x = np.linspace(-5, 5, 200)  #-5 到5 直接均匀的取200个点，返回的是ndarray类型
print(type(x))
y =np.sin(x)     #每个元素的正弦值
yn = y + random.rand(1, len(y)) *1.5    #加入噪声点集
#绘图
fig = plt.figure()   #创建一个图
# print(type(fig))
ax = fig.add_subplot(111)   #增加一个子图，位置为1,1,1,等价：fig.add_subplot(1, 1, 1)
print(type(ax))
ax.scatter(x, yn, c='blue')   #（x,yn）离散图,蓝色
ax.plot(x, y + 0.75, 'r')  #把y+0.75对x划线，红色
plt.show()
