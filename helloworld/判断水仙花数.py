#需求：用户输入一个三位数字，暂不考虑非数字，判断是否为水仙花数，个十百位上数字的三次方和位数本身。
#用户输入一个三位数字，暂不考虑非数字，
num = int(input('please enter the number(100~999):\n'))
if  not(100 <= num <= 999):
    print('InputError,program excit')
    exit()
# 判断是否为水仙花数，个十百位上数字的三次方和位数本身。
#num // 100 求整除方法得到百位上的数字
baiWei = num // 100
#num除100取余数之后再求整除得到百位上的数字
shiWei = (num % 100) // 10
#num除10求余得到个位数
geWei = num % 10
#判断是否为水仙花数
result = (baiWei ** 3 +shiWei ** 3 + geWei ** 3) == num
#打印结果
if result :
    print('YES!')
else:
    print('NO!')