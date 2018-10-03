#1、两个n维向量A（x11,x12,x13,,,,,,,,,,,,,x1n），B（x21,x22,x23,,,,,,,,,,,,,x2n）之间的闵可夫斯基距离为：
# sum = power(（x11 - x21）,p) + power(（x12 - x22）,p) + power(（x13 - x23）,p)+.......+ power(（x1n - x2n）,p)
#d12 = sqrt(sum, p),
# 当p=1时，为曼哈顿距离：差的绝对值之和: sum（abs（A - B））
# p=2时为欧式距离（坐标物理距离）:sqrt((A -B) * (A - B).T)
# p=∞时，为切比雪夫距离，即对应位置差的绝对值的最大值：abs(A - B).max()


#2、夹角余弦值：（A * B）/(|A| *|B|)    dot(A, B)/(linalg.norm(A) * inalg.norm(B))


#3、汉明距离：两个等长字符串s1，s2之间的汉明距离为：将其中一个变换为另一个所需要的最小替换次数。
from numpy import *
import numpy as np
matA = np.array([[1, 1, 0, 1, 0, 1, 0, 0, 1],
                 [0, 1, 1, 0, 0, 0, 1, 1, 1]])
matV = mat(matA)
smStr = nonzero(matV[0] - matV[1])   #返回非0元素的索引，是一个形式（array([0, 0, 0, 0, 0, 0], dtype=int32), array([0, 2, 3, 5, 6, 7], dtype=int32)）的元组，第0个位行号，第二个位列号
idx1 = np.transpose(smStr) #转置之后就可以组合成具体在二维数组中的索引
print(idx1)


#4、杰拉德相似系数：两个集合A、B的交集在A和B的并集中占的比例。是两个集合相似度的一种治标
#杰拉德距离：1- 杰拉德系数
import scipy.spatial.distance as dist
print(dist.pdist(matV, 'jaccard'))
# 算术平均：mean()
# 变量的协方差矩阵：cov()
#马氏距离：优点是量纲无关，排除了变量之间相关性的干扰
