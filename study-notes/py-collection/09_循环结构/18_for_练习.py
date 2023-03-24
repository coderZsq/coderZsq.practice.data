# 保证合法输入
n = 0
while n < 1 or n > 20:
    n = int(input('请输入[1, 20]范围的整数：'))

for i in range(n):
    print(('💚' if i % 2 else '❤') * n)

    # c = '💚' if i % 2 else '❤'
    # print(c * n)

    # if i % 2:
    #     print('💚' * n)
    # else:
    #     print('❤' * n)