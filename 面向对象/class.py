#类的创建遵循5大原则：
#1、单一原则：1个类只负责一个功能
#2、开放关闭原则：对扩展开放、对修改关闭
#3、里氏替换原则：使用基类引用的地方必须能使用继承类的对象（任何时候都可以用子类对象替换父类对象）
#4、接口分离原则：如果一个类包含过多的接口（简单理解为抽象方法）方法，而这些方法在使用的时候并非“不可分割”，那么应该把他们进行分离
#5、依赖倒置原则：高层模块不应该直接依赖低层模块，应该依赖抽象类或接口（如：电脑类不应该依赖鼠标类，而应该是鼠标类的一个抽象（能单击、双击、右击、移动指针），到时可以是无线鼠标、触摸板等）

#类的实例对象通过__class__属性而找的相应的类
#类的创建:type(类型，继承的类元组，类的属性和方法字典)
def run(self):
    """

    :param self:
    :return:
    """
    print(self)


xxx = type('Person', (), {'name': 'zyf', 'high': 180, 'weight': 63, 'run': run})   #创建一个类
person = xxx()   #将创建的类实例化
class Money:
    """
    类相关注释
    """
    # __slots__ = ['mianZhi', 'color']    #限制改类产生的对象添加的属性，也就是说Money类实例化的对象只能添加mianZhi、color两个属性
    moneyType = 'dollar'     #类属性（公有），可以通过类访问和实例访问
    _a = '这是一个受保护的属性，访问会出警告'
    __b = '这是私有属性，只能类内部访问'  #python无法实现真正私有，是通过名字重改机制实现的，如__x重改为：_class__x,不能版本python重改机制可能不一样
    def shi_li_method(self):
        print('这是一个实例方法', self)   #self是实例的地址，实例方法的第一个参数必须是实例
    @classmethod     #通过装饰器实现自动传递第一个参数
    def class_method(cls):
        print('这是一个类方法', cls)     #cls为类名，类方法的第一个参数必须是类；类方法只能访问类属性
    @staticmethod
    def stat_method():
        print('这是一个静态方法')        #第一个参数既不需要传递实例，也不需要传递类；不能直接访问对象属性和类属性
    #以上三种方法和类属性一样，都存储在类的__dict__属性字典里
print(Money.__name__)  #类名
money = Money()   #创建一个Money对象
money.mianZhi = 100    #创建一个对象属性：mainZhi，只能通过实例访问，不能通过类访问
money.color = 'red'
print(money.__dict__)  #dict函数访问所有的实例属性字典。
money.shi_li_method()   #实例方法的标准调用方法就是通过实例对象调用
money.class_method()    #通过实例也可以调用类方法，实例会被忽略，但实例对应的类会作为第一个参数传递过去，如果是子类调用则会把子类作为第一个参数传递
money.stat_method()
#通过实例可以调用所有存储在类中方法，而通过类名则不能调用实例方法
# Money.shi_li_method()   #通过类调用实例方法会报错，因为没有传第一个参数，确实第一个实例参数self
Money.class_method()
Money.stat_method()