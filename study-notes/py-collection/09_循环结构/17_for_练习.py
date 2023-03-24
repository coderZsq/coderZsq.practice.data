# 保证合法输入
n = 0
while n < 1 or n > 20:
    n = int(input('请输入[1, 20]范围的整数：'))

for i in range(n, 0, -1):
    print('❤' * i)

# for i in range(n):
#     print('❤' * (n - i))
