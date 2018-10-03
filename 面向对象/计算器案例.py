class Cal:
    def check_num(func):
        def inner(self, n):
            if not isinstance(n, int):
                raise TypeError('num type error,num should be a int object')
            return func(self, n)
        return inner
    @check_num
    def __init__(self, num):
        self.__res = num

    @check_num
    def jia(self,n):
        self.__res += n
        return self               #返回对象本身可以实现多次点调用，这种方式叫链式编程

    @check_num
    def jian(self,n):
        self.__res -= n
        return self

    @check_num
    def cheng(self,n):
        self.__res *= n
        return self

    @check_num
    def chu_yi(self,n):
        self.__res /= n
        return self

    def show(self):
        print('计算结果是：%d'%self.__res)


a = Cal(2)
a.jia(3)
a.jian(2)
a.cheng(3)
a.chu_yi(3)
a.show()
b = Cal(2)
b.jia(3).jian(2).cheng(3).chu_yi(3).show()