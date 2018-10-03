#输入身高、体重、年龄、性别
personHight = float(input('请输入身高（m）'))
personWight = float(input('请输入体重（kg）'))
personAge = int(input('请输入年龄'))
personSex = int(input('请输入性别(男：1 女：0)'))
#验证数据有效性,取非操作可以简化改代码量
if not (0 < personHight < 3 and 0 < personWight < 300 and (personSex == 0 or personSex == 1) and 0 < personAge < 150) :
    print('Input Error,the program will be eited')
    exit()
#计算体脂率
BMI = personWight / (personHight * personHight)
TZL = 1.2 * BMI + 0.23 * personAge - 5.4 -18.8 * personSex
#TZL = TZL * 100

#判断体脂率是否在正常范围之内
# minNum = 0.15 + 0.10 * (1 - personSex)
# maxNum = 0.18 + 0.10 * (1 - personSex)
# result = minNum < TZL < maxNum

#告诉用户是否在正常范围内
#print('您的体脂率是:%f%%,是否在正常范围内？'%(TZL) ,result)
#判断性别,不同性别赋予不同的数值
if personSex :
    wenhao = '先生您好，'
    minNum = 15
    maxNum = 25
else:
    wenhao = '女生您好，'
    minNum = 18
    maxNum = 28
result = minNum < TZL < maxNum
#判断体脂率情况，告知用户
if result :
    print(wenhao+'您的体脂率正常请继续保持！')
elif TZL > maxNum :
    print(wenhao+'您的体脂率偏高，身体偏胖！')
else :
    print(wenhao+'您的体脂率偏低，身体偏瘦！')