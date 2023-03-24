# 保证合法输入
n = k = 0
while n < 1 or n > 20:
    n = int(input('请输入第1个[1, 20]范围的整数：'))
while k < 1 or k > 20:
    k = int(input('请输入第2个[1, 20]范围的整数：'))

# n行k列
for _ in range(n):
    print('❤' * k)
