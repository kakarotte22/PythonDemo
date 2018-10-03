def func1():
    print('__name__ == main')


def func2():
    print('__name__ != main')

if __name__ == '__main__':
    func1()
else:
    func2()

