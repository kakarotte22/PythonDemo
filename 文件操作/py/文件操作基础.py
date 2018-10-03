import os
#导入os可以实现rename，renames，romove等函数的调用
#1、打开文件
f = open('test.txt', 'r')
#f是一个迭代器

#2、操作文件
#f.write('abc')
print(f.tell())  #tell函数返回当前的指针位置
f.seek(2, 1)      #往后移动当前指针2个位置,seek的第二个参数可以写（0,1,2）：0：最前面；（1：当前位置；2：末尾。只能在二进制文件中使用）
print(f.tell())
content = f.read()
#read函数比较耗内存，当操作文件很大时，可以使用readline函数，按需取某一行，或者采用for遍历


print(content)
print(f.tell())

#3、关闭文件
f.close()