# 保证合法输入
n = 0
while n < 3 or n > 20:
    n = int(input('请输入[3, 20]范围的整数：'))

for i in range(n):
    c = '💚' if 0 < i < n - 1 else '❤'
    print('❤' + c * (n - 2) + '❤')

# for i in range(n):
#     if i == 0 or i == n - 1:  # 最上面1行、最下面1行
#         print('❤' * n)
#     else:  # 其他行
#         print('❤' + '💚' * (n - 2) + '❤')

