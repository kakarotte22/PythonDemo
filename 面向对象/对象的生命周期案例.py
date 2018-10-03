class Person:
    __count = 0

    def __init__(self):
        print('new one')
        Person.__count += 1     #注意：此处千万不能写成self.__count += 1，因为self为实例对象，那样会给实例对象的__count 赋值

    def __del__(self):
        print('delete one')
        Person.__count -= 1

    @classmethod
    def num_count_print(cls):
        print(cls.__count)


p1 = Person()
p2 = Person()
Person.num_count_print()
del p1
Person.num_count_print()