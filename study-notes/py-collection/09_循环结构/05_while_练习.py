# 如果输入错误，要求重新输入
n = 0
while n < 1 or n > 100:
    n = int(input('请输入[1, 100]范围的整数：'))

# 如果输入正确，请打印以下计算结果（不准使用便捷的数学公式）
# 1 + 3 + 5 + 7 + ... + n（所有的奇数相加）

# 效率

ret = 0
i = 1
while i <= n:
    ret += i
    i += 2

print(f'结果为：{ret}')

# print('-------------------------')
#
# ret = 0
# while n >= 1:
#     ret += n if n % 2 else 0
#     n -= 1
#
# print(f'结果为：{ret}')

# while n >= 1:
#     if n % 2:
#         ret += n
#     n -= 1
