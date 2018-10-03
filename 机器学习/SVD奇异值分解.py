import numpy as np
import svdRec
from svdRec import *
from numpy import *
#A的每一行表示每一个用户，每一列表示每一种物品，数值表示为用户对物品的偏好。
A = np.array([[5, 5, 3, 0, 5, 5], [5, 0, 4, 0, 4, 4], [0, 3, 0, 5, 4, 5], [5, 4, 3, 3, 5, 5]])  #A的形状(6,4)
A = mat(A)
# A.H()   A的共轭转置
print(A)
a_SVD = np.linalg.svd(A)    #一个元组类型，有3个元素
print(type(a_SVD))
print(a_SVD.__len__())
print(a_SVD[0])   #第一个元素为u：向量，正交，（4，4）
print('*' * 30)
print(a_SVD[1])   #第二个元素为s：奇异值矩阵，ndarray，降序，（打印出为4个元素的list，是为了numpy节省空间的做法，因为除了对角线的元素为奇异值之外，其余都是0）
print(a_SVD[1][1])
print('奇异值的类型是：', type(a_SVD[1]), len(a_SVD[1]))
print('*' * 30)
print(a_SVD[2])   #第三个元素为vh：向量，正交（6,6）
print('*' * 30)
u = a_SVD[0]
s = a_SVD[1]
vh= a_SVD[2]

#原理A = u * sigma * vh
# 若保留r个奇异值，则A近似等于：u[：，：r] * sigma[:r, :r] * vh[:3, :]。u的前r列，vh的前r行
#其中：u会将物品(列)映射到A中；vh会将用户（行）映射到A中。通常用户数量远大于物品数量，为了节省计算时间，采用Item CF方式。
#给定一些用户行testV，采用Item CF方式，即将物品映射到空间去.   #result = testV * A--->result = testV *u[:,:r] *linalg.inv(sigma[:r, :r])
#保留奇异值个数r的取值问题：平方和接近总值90%；或根据经验取.
def get_sigma(r, s):
    zero = np.zeros((r, r))
    i = 0
    s = s.tolist()
    while i < len(s):
        zero[i][i] = s[i]
        i += 1
    return zero
#该函数等同于：return diag(s)[:r,:r]   等同于：eye（r） * s[]
r = 4
sigma = get_sigma(r, s)
# print(sigma.shape)
print(u[:, :r] * sigma * vh[:r, :])
print('END!')
#原理A =vh * 奇异值对角矩阵 * u.T
svdRec.recommends_for_user()  #创建一个svdRec实例，调用该方法可以