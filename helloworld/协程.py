#把函数编写成一个任务程序，用来处理发送给它的一系列输入，用（yield）的形式实现，用send（）发送数据
def print_matches(matchText):
    print('looking for', matchText)
    while True:
        line = (yield )   #接受一行文本
        if matchText in line:
            print(line)

match = print_matches('python')
match.__next__()    #必须调用next函数，协程才能执行第一个yield之前的语句，不调用next函数会报错
a = match.send('python')  #send（）函数的返回值为传递给下一个yield语句的值
print('a = ', a)
b = match.send('hello world')
print('b=', b)
c = match.send('python is cool')
print('c=', c)
match.close()   #协程一般会不断执行下去，直到显示关闭或者自己退出