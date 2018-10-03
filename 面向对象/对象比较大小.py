import functools


@functools.total_ordering   #通过该装饰器可以实现组合比较，如大于等于
class A:
    def __init__(self, age, weight):
        self.age = age
        self.weight = weight

    def __eq__(self, other):   #重构相等方法
        print("比较操作执行")
        return self.age == other.age

    def __gt__(self, other):  #大于，实现了大于比较，在使用其相反操作的时候（小于），系统会采用自动调换参数顺序的方法实现
        pass

    def __bool__(self):    #设定实例对象的bool值
        return True


a1 = A(18, 180)
a2 = A(18, 188)
print(a1 == a2)