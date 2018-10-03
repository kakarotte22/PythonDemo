#--------------------生成器----------------------------------------------
#生成器：特殊的迭代器，抽象层级更高。使用生成器可以不保存数据，只在next用的时候计算，省内存
#1、直接将表达式导出列表的方式中的[]换成（）
lst = (i for i in range(1, 101) if i % 2 == 0) #此时l式一个生成器，可通过for循环迭代和next（）函数访问；next函数不能将最后一个field语句后面的代码执行，而for遍历可以
print(lst)
print(next(lst))
print(next(lst))
print(lst.__next__())  #和上面的next（lst）式等同的


#2、生成器函数：函数中包含yield 语句，该函数的执行结果就是生成器
#yield 会阻断当前函数的执行，并把yield后面的状态值返回，当使用next（）函数时会继续执行，直到被下一个field语句阻断；遇到return就会抛出异常，并将return 后面的值返回
print('=' *30)
def ouShu():
    for i in range(1,11):
        if i % 2 == 0:
            yield i       #阻断程序执行，并返回i


g = ouShu()   #到当前位置为止，函数都未被执行，返回的是一个生成器，只有当执行next（）函数时，函数才会被启动
print(g)
for i in g:
    print(i)
g.close()   #关闭生成器 等同于将生成器指向最后一个
#.send（num）   可以给上一次yield语句一条返回值，为num，send与next一样也会继续执行，指定碰到新的yield语句