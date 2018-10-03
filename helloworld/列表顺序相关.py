#------------------------------列表升降序----------------------------------------------------------------------
#sorted（iterable，key=none，reverse=false）返回一个排好序的列表。key为排序关键字，值为一个函数，且函数只有一个参数，返回一个值用来比较,默认false升序,不改变列表本身
num =[('c',2),('a',5),('b',4),('d',3),('e',1)]
print(num,sorted(num))
def getKey(x):
    return x[1]
result = sorted(num,key= getKey)
#getKey不加（），加了表示调用，不加表示指向
print(result)
#列表对象方法：.sorted(key=none,reverse=false)  直接改变列表本身,返回none。key同内置函数sorted
num = [('c',2),('a',5),('b',4),('d',3),('e',1)]
result = num.sort()
print(result,num)
#------------------------------列表乱序----------------------------------------------------------------------
#import random
#random.shuffle(list)   返回none，直接改变列表
import random
num =[1, 2, 3, 4, 5, 6, 7, 8]
res = random.shuffle(num)
print(res,num)

#------------------------------列表乱反转----------------------------------------------------------------------
#l.reverse()  改变列表，返回none
num = [1, 2, 3, 4, 5, 6, 7, 8]
res = num.reverse()
print(res,num)


#切片反转：l[::-1]   不改变列表，返回反转后的列表
num = [1, 2, 3, 4, 5, 6, 7, 8]
res = num[::-1]
print(res,num)