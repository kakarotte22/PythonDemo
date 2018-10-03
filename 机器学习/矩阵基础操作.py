import numpy as np
from numpy import *
myZero = np.zeros((3, 5))  #生产3行5列的0矩阵
print(myZero)
myZero.A
print('*' * 30)
myOne = np.ones((5, 3))   #生产5行3列的元素全为1矩阵
print(myOne)
print('*' * 30)
myEye = np.eye(4)      #单位矩阵
print(myEye)
print('*' * 30)
myRand = np.random.rand(3, 4)
print(myRand)     #生成3行4列的0~1之间的随机数矩阵
print('*' * 30)
#两个矩阵的‘+’、‘-’运算为矩阵各个元素的加减
myRand1 = np.random.rand(3, 4)
print(myRand1)
myRand2 = np.random.rand(3, 4)
print(myRand2)
print('*' * 30)
print(myRand2 + myRand1)
#sum（矩阵M）：矩阵所有元素和
#num * M:一个数乘以矩阵M
#multiply（M1, M2）：表示矩阵对应元素的相乘，两个矩阵必须行列数都相同
#矩阵的n次幂：power（M，n）
#矩阵的乘法：M1 * M2
#矩阵的转置：M.T    或者M.transpose()
#M[idx]   :行切片
#M.T[idx]  ：列切片
#M1 < M2    ：对应元素的比较大小
(m, n) = myRand1.shape   #矩阵的行、列数
print(m, n)
print('*' * 30)
#矩阵的行列式：linalg.det(M)   M为方阵    (矩阵A的行列式detA就是线性变换A下的图形面积或体积的伸缩因子)
#矩阵的秩（非0子式的最高阶数）：linalg.matrix_rank(M)
print(linalg.det(myEye))
print(linalg.matrix_rank(myRand1))
#矩阵的对称：M * M.T
print('*' * 30)
m = np.matrix('[1, 2; 3, 4]')
#逆矩阵： .I  或者M.getI（）
print(m.I)
print(m.getI())
#向量范数：向量到原点的距离：linalg.norm(M)
print(linalg.norm(myEye))
# 逆矩阵：linalg.inv(M)
# diag(v, k=0)  构造对角阵，k表示对角线与主对角线的关系