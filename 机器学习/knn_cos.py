import numpy as np
from numpy import *
import operator
# from Nbayes_lib import *


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