import numpy as np
from numpy import *
import matplotlib.pyplot as plt
#1、消元求解
a = np.array([[8, -3, 2], [4, 11, -1], [6, 3, 12]])
# print(a,type(a))
b = np.array([20, 33, 36])
result = np.linalg.solve(a, b)     #当a，b都是矩阵的时候，参数就应该是b.T,这里都是ndarray
print(result, type(result), len(result))
print('*' * 30)

#-------------------------------------------------------------------------------------------------------------

#2、迭代求解,又叫逐次逼近法，在训练大型数据集的时候使用
#原理：对于给定方程组x = b0 * x +f，，(由方程组AX=B变换而来)使用公式：x^(k+1) = b0 * x^k +f ,
# 其中k为迭代次数，如果k->∞时，x^(k+1)存在，称此迭代法收敛，极限值就是方程组的解，否则称此迭代法发散
f = np.array([20/8, 3, 3])
f = mat(f)    #当计算2-D矩阵的时候，就要注意用np.array和mat数据类型的区别，使用乘法方面也不一样，最好是都用矩阵，即mat生成
b0 =np.array([[0, 3/8, -2/8], [-4/11, 0, 1/11], [-6/12, -3/12, 0]])
b0 = mat(b0)
#把原多项式转换成x1=***;x2=***;x3=***的形式，可以得到b0和f
error = 1.0e-6
steps = 100
xk = zeros((3, 1))
errorList =[]
for k in range(steps):
    xk_1 = xk
    xk = b0 * xk + f.T
    errorList.append(np.linalg.norm(xk - xk_1))
    if errorList[-1] < error:
        print('迭代次数：', k + 1)
        break
print(xk)
#绘制误差点集
matplt = zeros((2, k + 1))
matplt[0] = linspace(1, k + 1, k +1)
matplt[1] = array(errorList)
fig = plt.figure()   #创建一个图
# print(type(fig))
ax = fig.add_subplot(111)   #增加一个子图，位置为1,1,1,等价：fig.add_subplot(1, 1, 1)
ax.scatter(matplt[0], matplt[1], c='blue')   #（x,yn）离散图,蓝色
plt.show()
print('*' * 30)

#-------------------------------------------------------------------------------------------------------------

#3、
