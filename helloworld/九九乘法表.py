num1 = num2 =range(1 , 10)
for l in num1:
    for h in num2:
        if h <=l:
            print('%d * %d = %d'%(h,l,h*l),end='\t')
    print('')
        # elif h == l:
        #     print('%d * %d = %d' % (h, l, h * l))
        # else:
        #     break