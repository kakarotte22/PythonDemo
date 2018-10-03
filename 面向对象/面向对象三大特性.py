# MRO:Method Resolution Order,即方法解析顺序
#super:沿着MRO链条，找到下一级节点，并调用相应的方法：尽量全部使用super方法调用
#suoer(参数1[,参数2])：沿着参数2的mro链条，找到参数1的下一个节点，返回下一个节点
# def super(cls,inst):
#     mro = inst.__class__.mro()
#     return  mro[mro.index(cls) +1]
#如何应对类方法、静态方法以及实例方法的传参问题：使用参数2进行调用（第二个参数会被传送调用的方法内作为参数）
#3.x版本：super（）
#python中无法直接实现抽象类(不能直接创建实例，创建会报错)和抽象方法（不具体实现，不能直接调用，子类必须实现该方法），需要：
#1、导入abc模块：import abc
#2、设置类的元类为：abc.ABCMeta
#3、使用装饰器修饰抽象方法：@abc.abstractmethod


class A:
    def __init__(self):
        self.a = 'a'
    pass


class B(A):
    def __init__(self):
        super().__init__()   #等同于 ： super(B, self).__init__()
        self.b = 'b'
    pass


b = B()
print(b.a)