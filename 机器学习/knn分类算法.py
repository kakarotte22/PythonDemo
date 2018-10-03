#1、朴素贝叶斯算法：P(A)*P(B|A) = P(B)* P(A|B)
#2、如果一个样本在特征空间中的k个最邻近（最相似）的样本大多数都属于某一个类别，则该样本也属于这个类别
#knn算法分类，并且距离计算采用的是夹角余弦值。
import numpy as np
from numpy import *
import operator
# import sys
# path = 'D:\PythonDemo\机器学习'
# sys.path.append(path)
# from .knn_cos import cosdist
# from .knn_cos import clssify
np.seterr(invalid='ignore')   #存在运行时警告，这里设置忽略
def creat_data_set():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    lables = ['A', 'A', 'B', 'B']
    return group, lables


def cosdist(vector1, vector2):
    return dot(vector1, vector2)/(linalg.norm(vector1) * linalg.norm(vector2))


def clssify(testDate, trainSet, listClasses, k):   #listClasses:类别标签
    dataSetSize = trainSet.shape[0]   #返回样本集的行数
    distances = array(zeros(dataSetSize))
    for index in range(dataSetSize):
        distances[index] = cosdist(testDate, trainSet[index])
    sortedDistIndicies = argsort(-distances)   #返回对数据排序的索引，这里是-distances表示从余弦值从大到小排列，越大说明夹角越小
    classCount = {}
    for i in range(k):   #获取角度最小的前k项作为参考项
        voteIlabel = listClasses[sortedDistIndicies[i]]  #按排序顺序返回样本集对应的类别标签
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1  #为字典clssCount赋值（标签，标签出现次数），如果key相同，则value +1，如果不存在则赋值为0
        #get(key， default) 函数返回指定键的值，如果值不在字典中返回默认值
        sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
        #sorted(可迭代对象，key=operator.itemgetter(1),reverse = True)是sorted的固定用法
        return sortedClassCount[0][0]


#画图
dataSet, labels = creat_data_set()
# print(dataSet, labels)
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
index = 0
for point in dataSet:
    if labels[index] == 'A':
        ax.scatter(point[0], point[1], c='blue', marker='o', linewidths=0, s=300)
        plt.annotate('A', xy=(point[0], point[1]))
        # print(point)
    else:
        ax.scatter(point[0], point[1], c='red', marker='^', linewidths=0, s=300)
        plt.annotate('B', xy=(point[0], point[1]))
    index += 1
# plt.show()
#测试一个点属于哪一个类，绘图
testData = [0.2, 0.2]
ax.scatter(testData[0], testData[1], c='green', marker='*', linewidths=0, s=300)
plt.show()
print(clssify(testData, dataSet, labels, 3))