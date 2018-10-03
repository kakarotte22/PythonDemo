#描述器：可以描述一个属性操作的对象，必须实现属性的：__set__   __get__   __delete__方法，且必须都是新式类
#可以用@property 装饰器实现
#可以用 age = property（__set__，__get__，__delete__）实现
#最佳方法是把该属性操作封装在一个类里面，并实现__set__，__get__，__delete__方法
#资料描述器：实现了 __get__、 __set__
#非资料描述器:只实现了__get__
#优先级：资料描述器 >实例属性>非资料描述器
class Age:
    def __get__(self, instance, owner):   #重写了__getattribute__方法后会影响该方法的调用(instance:实例)
        # print('get')
        return isinstance.v

    def __set__(self, instance, value):
        # print('set')
        instance.v = value      #把赋值数据存储到age实例对象的v属性中去

    def __delete__(self, instance):
        print('delete')
        del instance.v

class Person:
    age = Age()


p = Person()
p.age = 10   #自动调用Age类里面的set方法（通过实例操作） 参数传递为：self = age;instance = p;value = 10
print(p.age)  #自动调用Age类里面的get方法，但get方法没有返回值，故打印none
del p.age       #自动调用Age类里面的delete方法