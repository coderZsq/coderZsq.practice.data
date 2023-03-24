# 保证合法输入
n = 0
while n < 1 or n > 20:
    n = int(input('请输入[1, 20]范围的整数：'))

# ❤❤❤
# ❤❤❤
# ❤❤❤

# end用来设置结束符
# print('❤', end='') 1
# print('❤', end='') 2
# print('❤', end='') 3
# print()
#
# print('❤', end='') 4
# print('❤', end='') 5
# print('❤', end='') 6
# print()
#
# print('❤', end='') 7
# print('❤', end='') 8
# print('❤', end='') 9
# print()

# print('❤', end='') 1
# print('❤', end='') 2
# print('❤', end='\n') 3
#
# print('❤', end='') 4
# print('❤', end='') 5
# print('❤', end='\n') 6
#
# print('❤', end='') 7
# print('❤', end='') 8
# print('❤', end='\n') 9

for i in range(1, n * n + 1):
    end = '' if i % n else '\n'
    print('❤', end=end)
    # if i % n:
    #     print('❤', end='')
    # else:
    #     print('❤', end='\n')

# for i in range(1, n * n + 1):
#     print('%02d' % i, end=' ')
#     # print('❤', end='')
#     if i % n == 0:
#         print()

# for i in range(n * n):
#     # print('%02d' % i, end=' ')
#     print('❤', end='')
#     if (i + 1) % n == 0:
#         print()

# line = '❤' * n
# for _ in range(n):
#     print(line)

# for _ in range(n):
#     # 每执行1次循环体，就打印1行数据
#     print('❤' * n)