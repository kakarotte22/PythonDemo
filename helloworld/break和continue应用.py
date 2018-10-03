while True :
    num1 = float(input('请输入第一个数字(0,100)：'))
    if not(0 <= num1 <= 100) :
        print('InputErr')
        continue
    num2 = float(input('请输入第二个数字(0,100)：'))
    if not(0 <= num1 <= 100):
        print('InputErr')
        continue
    result = num1 + num2
    print(result)
    isQ = input('任意键继续，q退出！')
    if isQ == 'q':
        break
