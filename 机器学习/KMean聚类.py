import numpy as np
from numpy import *
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
np.linalg.svd()      #奇异值分解，返回u，s,vh,其中u:左奇异向量（正交单位矩阵）；s：SIGMA，对角线元素为奇异值，降序，且减小速度特别快，
# 从存储来说，前10%甚至1%的奇异值之和就占了全部奇异值之和的99%以上；vh，右奇异向量（正交单位矩阵） 
dataset = mat()
kmeans = KMeans(init='k-means++', n_clusters=4)   #创建一个KMean类的实例
kmeans.fit(dataset)   #计算KMean聚类
#绘图，数据可视化
pass