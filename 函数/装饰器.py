#-----------------------装饰器----------------------------------------------------------------
#装饰器：在不改变函数名和函数体的前提下，给函数增加一些额外代码.(利用闭包的特性实现不改变函数单一功能且不改变业务逻辑代码，注：装饰器是立即执行的)
#语法：函数上面一行加语句：@额外代码块或函数


# class ChekLogin:
#     def __init__(self, needBeDecFunc):
#         self.f = needBeDecFunc    #因为@CheckLogin（语法糖）   等同于语句：fss = CheckLogin(fss)，创建一个CheckLogin实例，参数为fss函数，并赋值给fss，在执行 CheckLogin(fss)时会调用init函数，需要将原被装饰的函数存储在实例对象的一个属性中去，因此业务逻辑模块中，被装饰函数就成了装饰器的一个实例，当调用被装饰函数的时候，就需要实现call函数，在call函数中加入需要添加的代码块，并执行被装饰函数即可
#
#     def __call__(self, *args, **kwargs):   #实现该方法可以做到：实例对象可以像调用方法一样被调用，执行该方法
#         print('验证登录.......')
#         self.f()


def chekLogin(needDec):   #needDec  需要被装饰的函数，也可以用类来实现，如ChekLogin类
    def inner(*args, **kwargs):#inner函数里面加上通用参数可以实现装饰器通用，可以装饰具有不同参数长度的函数，此为约定俗成的做法，名称也可以更改，注意inner函数体格式应该与被装饰函数体一致
        print('验证登录.......')
        res = needDec(*args, **kwargs)
        return res       #被装饰的函数内有返回值也是需要保持同样格式
    return inner        #inner函数实际上就是指向被装饰的函数，将inner返回
#该装饰器已经为通用装饰器，可以装饰不同参数，和是否有返回值

# @chek_login
@chekLogin   #等同于语句：fss = checkLogin(fss)
def fss():
    print('发说说')


@chekLogin
#@checkLogin   等同于在函数后面   执行了一条语句：ftp = checkLogin(ftp)
def ftp():
    print('发图片')

@chekLogin
def flj(str):
    print(str)
#相关业务逻辑代码
index = 3
if index == 0:
    fss()
elif index == 1:
    ftp()
else:
    flj('www.baidu.com')
#以上代码实现了在发说说和发图片之前验证登录，而不变更业务逻辑代码，且不违反函数单一功能原则