#迭代器：任何实现了__iter__()和__next__()方法的对象都是迭代器
l = [1, 2, 3, 4, 5, 6, 7, 8]
itr = iter(l)
for i in itr:
    print(i)