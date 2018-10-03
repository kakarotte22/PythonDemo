#--------------------------------获取列表单个元素------------------------------------------------------
num = range(1,10,2)
print(num[3])
#--------------------------------获取列表某个元素的索引--------------------------------------------
#.index(obj,start=0,stop=lst.len()),如果有多个则返回区间内第一个
print(num.index(7))

#--------------------------------获取列表某个元素个数------------------------------------------------------
#.count(obj),返回元素obj在列表中的个数
num = [1, 2, 2, 3, 4, 2, 4, 5]
print(num.count(4))
#--------------------------------获取列表多个元素------------------------------------------------------
# itms[start : end : step ]
print(num[2 : 5 : 1])
#列表反转
print(num[::-1])
#--------------------------------列表的遍历------------------------------------------------------
#根据元素进行遍历，并同时打印当前元素对应的索引值
currentIdx = 0
for v in num:
    print(v,num.index(v,currentIdx))
    currentIdx += 1
#根据索引遍历
num = [1, 2, 2, 3, 4, 2, 4, 5]
for idx in range(len(num)):
    print(num[idx],end="\n")
#创建枚举对象遍历 (key,value)
#enumerate(itrObj,[start=0]):itrObj为一个序列、迭代器或其他支持迭代的对象
a = enumerate(num)
# print(list(a))
for i in a:
    idx,val = i
    print(idx,val)
# a1,a2=(a,b)执行之后a1==a;a2==b
#判断是否可迭代：import collections       isinstance(object, classinfo)