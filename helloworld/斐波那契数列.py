import time
a, b = 0, 1
# print(a)
fbnqlst = [a, b]
max = eval(input("您需要多大以内的菲波那切数列？"))
start = time.clock()
while a+b < max:
    # print(b, end=',')
    a, b = b, a + b
    fbnqlst.append(b)
else:
    for le in fbnqlst :
        print(le,end=',')
    print('End!')
    # print(zhishulist)
end = time.clock()
print(end - start)