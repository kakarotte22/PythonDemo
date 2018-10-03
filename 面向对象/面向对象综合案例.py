import inspect
#inspect.getmro(class)   或  class.mro()   返回class类的资源查找顺序  3.x版本全是新式类，采用C3算法
#需求：定义猫、狗、人三个类
#狗：姓名、年龄（默认1）：吃饭、玩、睡觉、看家（格式：我的名字是xx，年龄xx的小狗在XX）
#猫：姓名、年龄（默认1）：吃饭、玩、睡觉、捉老鼠（格式：名字是xx，年龄xx的小狗在XX）
#人：姓名、年龄（默认1），宠物：吃饭、玩、睡觉、捉老鼠（格式：名字是xx，年龄xx的小狗在XX）
#                               养宠物（让所有的宠物吃饭、玩、睡觉）
#                               让宠物工作（让所有的宠物根据自己的职责开始工作）
#--------------------------------代码实现------------------------------------------------------------------------
#需求：定义猫、狗、人三个类
import abc


class Animal:
    def __init__(self, name, age):
        if isinstance(name, str) and isinstance(age, int):
            if 0 < age < 200:
                self.age = age
                self.name = name
            else:
                print('age error')
        else:
            print('格式错误！')

    def eat(self):
        print('%s eat' % self)

    def drink(self):
        print('%s drink' % self)

    def sleep(self):
        print('%s sleep' % self)

    def play(self):
        print('%s play' % self)

    def __str__(self):
        return '我的名字是{}，年龄{}岁的{}在'.format(self.name, self.age, self.__class__.__name__)


class Dog(Animal):
    def job(self):
        print('%s kan_jia' % self)


class Cat(Animal):
    def job(self):
        print('%s catch_mouse' % self)


class People(Animal):
    def __init__(self, name, pet, age=1):
        super().__init__(name, age)
        self.pets = pet

    def yang_pets(self):
        pet: Animal
        for pet in self.pets:
            pet.eat()
            pet.drink()
            pet.play()
            pet.sleep()

    def pets_job(self):
        for pet in self.pets:
            pet.job()


d = Dog('dog-d', 5)
c = Cat('cat-c', 7)
p = People('ZYF', [d, c], 28)
print(p.__dict__)
p.yang_pets()
p.pets_job()
# print(c.__class__.__name__)