#-----------------------带参数装饰器（根据不同情况生成不同装饰器）----------------------------------------------------------------
def getCheckLogin(char=''):
    def chekLogin(needDec):
        def inner(*args, **kwargs):
            print('验证登录' + char * 30)
            res = needDec(*args, **kwargs)
            return res
        return inner
    return chekLogin    #将装饰器返回



# def chekLogin(needDec):
#     def inner(*args, **kwargs):
#         print('验证登录.......')
#         res = needDec(*args, **kwargs)
#         return res
#     return inner


@getCheckLogin('*')
#@checkLogin（语法糖）   等同于语句：fss = checkLogin(fss)
def fss():
    print('发说说')


@getCheckLogin('=')
#@checkLogin   等同于在函数后面   执行了一条语句：ftp = checkLogin(ftp)
def ftp():
    print('发图片')

@getCheckLogin('+')
def flj(str):
    print(str)
#相关业务逻辑代码
index = 1
if index == 0:
    fss()
elif index == 1:
    ftp()
else:
    flj('www.baidu.com')
#以上代码实现了在发说说和发图片之前验证登录，而不变更业务逻辑代码，且不违反函数单一功能原则