#列表：有序、可变的元素集合，lis = [2,'str',True,'\n',[2,3,4]]
#----------------------------列表产生-------------------------------------------------
# lst = range(1,99,2)
# print(lst)
#----------------------------列表推导出新列表-------------------------------------------------
#[表达式 for 变量 in 列表 if 条件]
lst = [1, 2, 3, 4, 5]
resultLst = [num ** 2 for num in lst if num % 2 != 0]
print(resultLst)
#----------------------------列表增加，改变原列表-------------------------------------------------
#append（obj）：末尾增加列表元素,没有返回值，所有 print（lst.append(5)）为None,obj直接作为一个元素追加到末尾
lst.append('wo shi zhui jia de')
print(lst)
#insert（index,object）:将object插入在index位置前，没有返回值
lst.insert(3, 'obj')
print(lst)
#extend(iterable):往列表中扩展另一个可迭代序列，没有返回值，将iterable中元素拆开追加到末尾
num = [1, 2, 3]
str = 'abc'
num.extend(str)
print(num)
#列表乘法：lst * (int)n  :将列表内所有元素重复n次
lst = [1, 2, 3]
print(lst * 3)
#列表加法，只能列表+列表，不能为字符串
num1 = [1, 2, 3]
num2 = ['a','bcd', 4]
num3 = 'abcd'
print(num1 + num2)
#print(num1 + num3) 此行会直接报错，不能加字符串
#----------------------------列表删除，改变原列表-------------------------------------------------
# del 语句：可以删除一个变量、列表或某个元素如：num = 10    del num   那么num变量将被删除
del num2[1]
print(num2)
# .pop(index=-1):移除并返回列表中指定索引对应的元素；返回值为被移除的元素
num = [1, 2, 3, 'abc', 3]
result = num.pop(1)
print(result, num)
#.remove(obj):移除列表中的指定元素，如果元素不存在会报错，如果存在多个会移除最左边的一个，返回值为None；注意遍历移除的坑
result = num.remove(3)
print(result, num)
#移除列表中所有的某个值的元素做法（不能再循环遍历体中移除）:遍历查找看有多少个，之后遍历移除那么多次。
num = [1, 2, 3, 'abc', 3, 4, 5, 3, 3, 3, 3, 3, 4, 5, 3, 4]
count = 0
for a in num :
    if a == 3:
        count +=1
while count :
    num.remove(3)
    count -=1
print(num)
#----------------------------列表修改，改变原列表-------------------------------------------------
#修改列表：当我们想要操作列表中某个元素时，一定是通过索引（下标）来操作指定元素
num = [1, 2, 3, 'abc', 3, 4, 5, 3, 3, 3, 3, 3, 4, 5, 3, 4]
num[3] = 4
print(num)
