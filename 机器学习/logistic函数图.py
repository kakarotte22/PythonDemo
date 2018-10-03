import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.lines as pltln
from matplotlib.lines import Line2D
x = np.linspace(-20, 20, 500)
y = 1/(1 + np.e ** -x)
fig = plt.figure()   #创建一个图
# print(type(fig))
ax = fig.add_subplot(111)   #增加一个子图，位置为1,1,1,等价：fig.add_subplot(1, 1, 1)
plt.plot(x, y)
plt.plot([0, 0], [0, 1])
plt.plot([-20, 20], [0.5, 0.5])   #绘制（-20,0.5），（20,0.5）的连线
plt.title('Func:logistic')
plt.show()