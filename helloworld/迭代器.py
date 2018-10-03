import collections
lst = [1, 2, 3, 'asd', True, 5]
#1、创建一个迭代器(可以自动记录当前位置，从第一个元素开始，通过next（）函数往后，不能往前，迭代完之后继续next迭代会报错StopIteration，一般不能多次迭代)
it = iter(lst)
# isIter = isinstance(it, collections.Iterator)
# print(isIter)
#2、通过迭代器遍历
for v in it:
    print(v)
#本行执行之后it不会继续迭代了，如需继续迭代需要重新创建迭代器
