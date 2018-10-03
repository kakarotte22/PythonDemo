#-------------------------------------字符串查找相关----------------------------------不改变原字符串
#计算字符串长度
name = '  abcdefg hijklmn ABCDEFG-HIJKLMN    |'
lenth = len(name)
print(lenth)
#查找字符串(从左向右) 找不到返回-1，找到返回下标
num = name.find('cf',4,20)
print(num)
#查找字符串(从右向左边)，同find
num = name.rfind('cd')
print(num)
#计算某个子字符串出现的个数
print(name.count('abc',0,7))
#-------------------------------------字符串转换相关----------------------------------不改变原字符串
#用新字符串替换原旧字符串,replace不会更改原字符串
#替换个数count
count = 1
print(name.replace('b','B',count))
print(name)
#首字母大写，不会改变原字符串
print(name.capitalize())
print(name)
#将字符串中每个单词的首字母变为大写，不改变原字符串，凡中间不是字母的，都看作分隔符，之后都看成单词，汉字没有大小写
print(name.title())
print(name)
#字符串字母全部变为大写、小写，不改变原字符串
print(name.lower())
print(name)
print(name.upper())
print(name)
#-------------------------------------字符串填充压缩相关----------------------------------不改变原字符串
#ljust:根据指定字符（1个），将原字符串填充够指定长度；l表示原字符串靠左;不改变原字符串；如果原串长度大于需求长度则不填充
print(name.ljust(50,'*'))
# print(name)
#rjust:根据指定字符（1个），将原字符串填充够指定长度；r表示原字符串靠右;不改变原字符串；如果原串长度大于需求长度则不填充
print(name.rjust(50,'*'))
# print(name)
#center:根据指定字符（1个），将原字符串填充够指定长度；center表示原字符串居中;不改变原字符串；如果原串长度大于需求长度则不填充
print(name.center(50,'*'))
# print(name)
#lstrip：移除原字符串中指定字符集合,默认为空格；l表示仅仅移除左侧的(rstrip为移除右侧的):从左侧还检索，查到则移除，没查到就结束
name ='abcdeABCDE'
print(name.lstrip('abAB'))
print(name)
#-------------------------------------字符串分割拼接相关----------------------------------不改变原字符串
#split(sep,maxsplit):将一个大的字符串分割成几个子字符串，按照sep分割符分割，分割maxsplit次，返回分割后的子字符串列表
name = 'zyf-28-man'
print(name.split('-',2))
#partition:根据指定的分割符，返回元组：（分割符左侧的内容，分割符，分割符右侧的内容）；如果没找到分割符，返回（原字符串，‘’，‘’）
print(name.partition('-'))
#rpartition：表示从右侧开始检索
print(name.rpartition('-'))
#splitlines(keepends):按照换行符（\r,\n）将原字符串拆成多个元素，保存到列表中；keepends表示是否保留换行符，bool类型,默认false
#'\r' 回车，回到当前行的行首，而不会换到下一行，如果接着输出的话，本行以前的内容会被逐一覆盖
name = 'wo \n you \r ta'
print(name.splitlines(True))
#join（iterable）：根据指定字符串，将给定的可迭代对象（可以使用for循环进行遍历的都是，如list、元组、字符串。。。），进行拼接，得到拼接后的字符串
it =['zyf','28','man','025-18115054967']
print('-'.join(it))
#-------------------------------------字符串判断相关----------------------------------不改变原字符串
#isalpha（）：字符串中是否所有的字符全是字母，不包含数字、特殊符号、标点符号、换行空格等，且至少要有1个字符(空串返回false)，返回bool类型
name = 'zyf1'
print(name.isalpha())
#isdigit():字符串中是否所有的字符全是数字，不包含字母、特殊符号、标点符号、换行空格等，且至少要有1个字符(空串返回false)，返回bool类型
name = '789'
print(name.isdigit())
#isalnum():字符串中是否所有的字符全是字母或数字，不包含特殊符号、标点符号、换行空格等，且至少要有1个字符(空串返回false)，返回bool类型
name = 'abc123'
print(name.isalnum())
#isspace():字符串中是否所有的字符全是空格（缩进、回车、换行等不可见转义字符）
name = '\r '
print(name.isspace())
#startswith(prefix,start = 0,end = len(str)):判断一个字符串是否以指定前缀开头
name = '2018-9-14:xxxx.ppt'
print(name.startswith('2018-9-13'))
#endswith(prefix,start = 0,end = len(str)):判断一个字符串是否以指定后缀结尾
print(name.endswith('.ppt'))