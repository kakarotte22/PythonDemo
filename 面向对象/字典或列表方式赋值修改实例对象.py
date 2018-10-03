class A:
    def __init__(self):
        self.l = [1, 2, 3, 4, 5, 6, 7]

    def __setitem__(self, key, value):   #key为slice类对象的一个实例,当实例使用列表或字典方式赋值操作的时候自动调用该方法
        self.l[key] = value
        print(key.start)
        print(key.stop)
        print(key.step)
        print(value)

    def __getitem__(self, item):        #当实例对象采用列表或字典方式获取操作(遍历、访问)的时候自动调用该方法
        return self.l[item.start: item.stop: item.step]

    def __iter__(self):    #重构该方法，当在遍历实例对象的时候会调用，必须返回一个迭代器，且优先级高于实现__getitem__方法
        return iter(self.l)

    def __next__(self):   #与iter组合，必须设置终止条件
        i = 0  #添加这一条语句可以实现迭代器的重复使用，正常情况下一次迭代完毕之后指向了末尾，多了这条语句指向了开头
        if i < self.l.__len__():
            return self.l[i]
        else:
            raise StopIteration('END!')

    def __delitem__(self, key):
        del self.l[key]

    def __str__(self):
        return str(self.l)

a = A()
a[0: 4: 2] = ['a', 'b']   #执行到该条赋值语句时会自动调用__setitem__函数，key被赋值为[0: 4: 2]的slice实例，并完成相应的赋值操作
# print(a.l)
print(a[0: 6: 1])
del a[1]
print(a)
for i in a:
    print(i)
