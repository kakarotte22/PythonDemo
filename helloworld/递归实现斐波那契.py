def fibonacci(n):
    '''

    :param n: 菲波那切数列的第几位数，第0位是0，第1位是1
    :return: 第n位菲波那切数列的值
    '''
    if (n == 0 or n == 1):
        return n
    return fibonacci(n - 1) + fibonacci( n - 2)

for i in range(0, 8):
    print(fibonacci(i))