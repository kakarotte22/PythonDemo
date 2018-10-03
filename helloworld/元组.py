#元组：有序的，不可变的集合（可哈希的）
#定义
t1 = (1,)
t2 = (1, '2', True, t1)
t3 = 1, '3', t2
print(type(t1), type(t2), type(t3),)
#从列表中转换
t1 = [1, 'sz', True]
ct = tuple(t1)
print(ct, type(ct))
print(t1[0:14:])