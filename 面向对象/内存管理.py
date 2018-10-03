#python 使用引用计数器机制、“标记-清除”和垃圾回收机制并存。计数器机制无法解决循环引用的问题，垃圾回收机制可以
import gc
import weakref
#------------自动回收-----------
print(gc.isenabled())   #查看垃圾自动回收机制是否开启
print(gc.get_threshold())  #查看当前机制的默认参数，返回元组（700,10,10）：新增对象个数-消亡对象个数 达到700触发，0代触发10次则触发0代和1代的检测，1代触发10次，会触发0代、1代和2代的检测
#-----------手动回收-------------

import objgraph
class Person:
    pass


class Dog:
    pass


p = Person()
d = Dog()
p.pet = d
d.master = p
#创造了一个循环引用，以后写代码的时候开业通过弱引用来规避循环引用,d.master = weakref.ref(p) 弱引用，不会造成计数器增减
del p
del d
gc.collect()   #参数不写，则回收所有代的垃圾
print(objgraph.count('Person'))   #打印Person类产生的对象有多少个
print(objgraph.count('Dog'))