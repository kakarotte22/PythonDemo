#程序内定一个数字，让用户猜，正确则提示正确，退出；错误则提示大了或者小了，继续猜
#程序内定一个数字
import random
num = random.randint(1,100)
# 让用户猜，正确则提示正确，退出；错误则提示大了或者小了，继续猜
#接收一个用户猜的数字

#判断对错
while True:
    userNum = int(input('please guss the num（1~100） :'))
    if userNum == num :
        print('Yes,Exit!')
        exit()
    elif userNum > num:
        print('大了,Going on!')
    else:
        print('小了,Going on!')