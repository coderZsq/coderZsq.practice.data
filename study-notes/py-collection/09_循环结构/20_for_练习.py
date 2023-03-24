# 保证合法输入
n = 0
while n < 1 or n > 20:
    n = int(input('请输入[1, 20]范围的整数：'))

for i in range(n):
    lr = '🖤' * (n - i - 1)
    print(lr + '❤' * (2 * i + 1) + lr)
