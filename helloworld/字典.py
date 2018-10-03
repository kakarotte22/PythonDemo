#字典：无序的、可变的键值对集合。key不可重复，不可变，如重复则前面的会被后面的覆盖
#----------------------------新建字典------------------------------------------------------------------------------
info = {'name': 'zyf', 'age': 28, 'sex': 1}
info1 = dict.fromkeys('abc', 666)
#dict.fromkeys('abc',666)     同{a:666,b:666,c:666}
print(info1)
#---------------------------字典的增、删、改-----------------------------------------------------------------
info['tel'] = '18115054967'
print(info)
#语句删除
del info['sex']
print(info)
#对象函数删除：.pop(key[,default]) 删除指定的键值对，返回对应的值，如果key不存在则不做删除，并返回给的default值，如果default也没给出则报错
info = {'name': 'zyf', 'age': 28, 'sex': 1}
d = info.pop('name1', 18)
print(d, info)
#删除按升序排列后的第一个键值对，并以元组的形式返回改键值对，如果字典为空，则报错
info = {'name': 'zyf', 'age': 28, 'sex': 1}
dlt = info.popitem()
print(dlt, info)
#清空字典内容，字典对象还在:  .clear()注意与del语句的差别，返回none
info = {'name': 'zyf', 'age': 28, 'sex': 1}
print(info.clear(),info)
#----------------------------修改单个键对应的值（key不能改） 同line 7---------------------------------
#批量修改value：oldDict.update(newDict):根据newDict中的键值对更新oldDict中的键值对，如果oldDict中不存在对应的key，则新增键值对,返回值为none
info = {'name': 'zyf', 'age': 28, 'sex': 1}
rt = info.update({'tel': '18115054967','age': 35})
print(rt, info)
#--------------------------字典查询相关--------------------------------------------------------------
#直接通过key获取：dic[key]
#函数获取：dic.get(key[,default]):key不存在则返回default值，如果没给定default则返回none，不会报错，不改变原字典
info = {'name': 'zyf', 'age': 28, 'sex': 1}
print(info.get('age1', 666))
#dic.setDefault(key[,default]):返回指定key对应的值，如果key不存在，则增加一个键值对：key：default，default未给则为none，
info = {'name': 'zyf', 'age': 28, 'sex': 1}
print(info.setdefault('age1', 666))
print(info)


info = {'name': 'zyf', 'age': 28, 'sex': 1}
#获取字典所有的值：dic.values(),返回的是字典视图对象，字典改变了，得到的视图对象也会改变，不管代码前后。（2.x版本是直接返回列表）
print(info.values())
#获取字典所有的键：dic.keys()
print(info.keys())
#获取字典所有的键值对：dic.items()
print(info.items())
#-------------------------遍历-------------------------------------------------------------
#1、通过key遍历
info = {'name': 'zyf', 'age': 28, 'sex': 1}
key = info.keys()
for k in key:
    print(k)
    print(info[k])
#2、直接遍历所有的键值对（推荐使用）
info = {'name': 'zyf', 'age': 28, 'sex': 1}
t = info.items()
info['adress'] = 'shanghai'
#即使在把键值对对象先赋值给了t，之后更改了字典，也不会影响遍历结果，这是字典视图对象的特性
for k, v in t:
    print(k, v)
#------------------------计算和判断---------------------------------------------------------------
#len（dic）：计算键值对的个数
info = {'name': 'zyf', 'age': 28, 'sex': 1}
print(len(info))
#判断：判断的是key，不是value： xx in dic;xx not in dic;返回bool类型


