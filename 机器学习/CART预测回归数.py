#数据可视化函数：
import matplotlib.pyplot as plt   #画图必须导入该包


def plot_figure(X, X_test, y, yp):   #注意矩阵对象不是1-D，不是1维的，调用tolist（）方法，转换成列表
    plt.figure()
    plt.scatter(X.tolist(), y, c='k', label='data')
    plt.plot(X_test.tolist(), yp.tolist(), c='r', label='max_depth=5', linewidth=2)
    plt.xlabel('data')
    plt.ylabel('target')
    plt.title('Decision Trenn Regression')
    plt.legend()
    plt.show()


import numpy as np
from numpy import *
from sklearn.tree import DecisionTreeRegressor


x = np.linspace(-5, 5, 200)   #-5到5，均匀取200个点
siny = np.sin(x)
X = mat(x).T
print(X.shape)    #X.shape 为（200,1）
y = siny + np.random.rand(1, len(siny)) * 1.5   #加入噪声点集：y.shape（1,200）的随机噪声
# print(y.shape)
# print(y.tolist())
y = y.tolist()[0]   #y是一个嵌套list，取第0个，得list
clf = DecisionTreeRegressor(max_depth=4)   #选择深度为4的回归树
clf.fit(X, y)    #从（X,y）中构建一个回归树训练集，返回self


#预测回归
X_test = np.arange(-5.0, 5.0, 10/200)[:, np.newaxis]    #X_test.shape为（200,1）

print(X_test.shape)
yp = clf.predict(X_test)     #yp.shape:[200,]

print('yp.shape:', yp.shape)
print(type(yp))
# print('x')
# print(X.shape, X_test.shape, y1.shape, yp.shape)
plot_figure(X, X_test, y, yp)