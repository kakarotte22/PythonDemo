class Person(object):    #严格来说，使用属性装饰器应该继承object类，python 3.x版本默认继承object类
    def __init__(self):
        self.__age = 18     #构造函数在创建实例对象的时候就会自动调用,创建私有的age属性

    @property     #属性装饰器能够实现像读取属性一样使用方法
    def age(self):
        return self.__age   #公开私有age属性的获取接口，可以实现私有属性的只读操作

    @age.setter             #新式类中可以关联，经典类（没有继承object类）不可以
    def age(self, value):
        self.__age = value


p = Person()
#p.age = 20   #没有9-11行的情况下，只读属性赋值会报错
print(p.age)