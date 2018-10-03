#---------------------------方法1--------------------------------------------------------------------------------------------
# try:
#     可能出现异常的代码块（从上往下检测，检测到异常之后里面往下匹配，不会多次检测）
# except 要捕捉的异常类型 as 接受异常的形参：（可多个）             异常类型可以多个，组成元组，或分别写except，更或者直接用Except类名，接受异常的形参为要捕捉的异常的返回值
#     对于异常的处理
# else:
#     没有异常时的处理（可省略）
# finally:
#     不管有无异常都会处理（可省）
#---------------------------方法2--------------------------------------------------------------------------------------------
import contextlib
import traceback


class Test:
    """
    实现了__enter__和__exit__方法，叫上下文管理器,在使用上下文管理器处理异常的时候，不管中间body部分是否有异常，enter和exit都会被执行
    """
    def __enter__(self):
        print('enter')

    def __exit__(self, exc_type, exc_val, exc_tb):     #exc_type, exc_val, exc_tb        分别为异常类型，异常的值，异常的追踪(什么地方出错了)
        print(self, exc_type, exc_val, exc_tb)
        print(traceback.extract_tb(exc_tb))
        print('exit')
        return True      #返回true则异常不会返回给外界，否则会返回给外界，即报错

#x是Test（）实例中enter方法的返回值
with Test() as x:
    print('body', x)
    1/0
#----------------------方法2的简写--------------------------------------------------------------------------------------
import contextlib
#contextlib.closing(实现了close方法的对象)   把该对象变为上下文管理器，并把对象本身返回，即enter方法返回self


@contextlib.contextmanager      #把函数装饰城上下文管理器，配合yield使用
def demo():
    print('1')
    yield 'xxx'     #yield之前的代码会作为enter方法，之后的会作为exit方法，后面的值会传递给x
    print('3')


with demo() as x:
    print('2', x)