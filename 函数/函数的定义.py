#---------------------函数定义-----------------------------------------------------------
#注：函数应遵循单一原则：一个函数只实现一个功能
#指定参数赋值可以实现不按照顺序写实参
def myHs(num1, num2):
    print('num1：%d,num2:%d'%(num1 , num2))


myHs(3, 5)
myHs(num2=5, num1=3)
#def 函数名（*args）：参数为元组实现不定长参数     （*可以进行拆包、装包）
#         函数体
#控制台输入：help(函数名)  查看函数帮助

def noLongSum(*t):
    """
    实现不定长参数的和
    :param t: 可迭代对象
    :return: none
    """
    sum = 0
    itr = iter(t)
    for v in itr:
        sum += v
    print(sum)


noLongSum(3, 4, 5, 6, 7)
#def 函数名（**kwargs）：参数以字典实现不定长参数，但调用时必须使用关键字参数赋值的方式
#         函数体
#在python中，参数的传递全部是地址传递，参数为变量时，会改变原变量，参数不可变时则不会更改
#赋值语句：b = 666 实际操作是，在内存中开一个区域存放666，让b指向它，b实际是666的地址


#--------------------偏函数--------------------------------------------------------------
#偏函数：当我们写一个参数比较多的函数时，有些时候某些参数都是一个固定的值，为了简化使用可以创建一个新函数，指定要使用的函数的某个参数为固定值，这个函数就叫偏函数

import functools


def test(a, b, c, d, e):
    print(a + b + c + d + e)


newFuntest = functools.partial(test, d=5, e=5)
newFuntest(1, 2, 3)

#--------------------高阶函数--------------------------------------------------------------
#高阶函数：当一个函数A的参数也是一个函数的时候，称A为高阶函数
def cal(num1, num2 ,calFun):
    result = calFun(num1, num2)
    print(result)


def plus(num1, num2):
    return num1 + num2


def sub(num1,num2):
    return num1 -num2


cal(1, 2, plus)
cal(1, 2, sub)

#--------------------返回函数--------------------------------------------------------------
#返回函数：是指一个函数内部，返回得数据是另一个函数，称这样的操作为返回函数
def getFun(flag):
    """

    :param flag:只能为"+"或"-"
    :return: 函数
    """
    #内层函数引用了外层函数的变量或参数，外层函数又把内层函数作为返回值，这就叫闭包，当内部需要更改外部变量时，需要申明：nonlocal 外层变量
    def plus(num1,num2):
        return num1 + num2
    def sub(num1,num2):
        return num1 - num2
    if flag == '+':
        return plus
    else:
        return sub
def cal(num1,num2,flag):
    flagFun = getFun(flag)
    print(flagFun(num1, num2))


cal(5, 6, '+')
cal(5, 6, '-')


#--------------------匿名函数--------------------------------------------------------------
#lambda 参数1，参数2 。。。。: 表达式
#表达式的结果就是返回值，值适用于简单操作


























































































