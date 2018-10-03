class Person:
    """
    这是一个人,类
    """
    #setatter方法只有在使用'对象.属性 = 值'方式给实例增加一个属性，或者更改属性值的时候回调用，在这个方法内部才会真正将这个属性以及对应得值，存储到__dict__中
    def __setattr__(self, key, value):
        if key == 'age' and key in self.__dict__.keys():    #假设要设置age为只读属性
            print('这是一个只读属性，不能设置，更改')
        else:
            self.__dict__[key] = value

    def __str__(self):
        '''
        当以后出现print这个实例对象时会触发这个函数，主要用于格式化输出信息
        :return: 格式化的输出信息
        '''
        return '这个人的年龄是：%d' % self.age

    def __init__(self):
        self.dicAttr = {'name': 'zyf', 'high': 180}   #构造函数创建一个sx属性，为字典，当对象使用字典操作时可以实现存储到sx属性里

    def __getitem__(self, item):
        print('实现get、set、del三个内置函数可以把实例对象当成字典或列表一样操作,如索引，切片')
        return self.dicAttr[item]

    def __setitem__(self, key, value):
        print('实现get、set、del三个内置函数可以把实例对象当成字典或列表一样操作,如索引，切片')
        self.dicAttr[key] = value

    def __delitem__(self, key):
        print('实现get、set、del三个内置函数可以把实例对象当成字典或列表一样操作,如索引，切片')
        del self.dicAttr[key]

    def __call__(self, *args, **kwargs):
        print('实现该方法可以做到：实例对象可以像调用方法一样被调用，执行该方法')

p = Person()
p.age = 18     #此时会调用__setattr__方法,age此时不在字典里，故添加该属性和值
print(p.__dict__)
p.age = 99     #此时age已经存在在字典里，故不会再添加，也不会更改age的值
print(p.age)
print(Person.__bases__)   #父类元组
print(Person.__module__)  #类定义所在模块
print(Person.__doc__)    #类的说明文档
print(p)
print(p.dicAttr['name'])
p()