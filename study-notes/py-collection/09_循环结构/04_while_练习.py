# 如果输入错误，要求重新输入
n = 0
while n < 1 or n > 100:
    n = int(input('请输入[1, 100]范围的整数：'))

# 如果输入正确，请打印以下计算结果（不准使用便捷的数学公式）
# 1 – 2 + 3 – 4 + ... + n（所有的奇数相加，减去所有的偶数）

ret = 0
# 所有的奇数相加
i = 1
while i <= n:
    ret += i
    i += 2

# 减去所有的偶数
i = 2
while i <= n:
    ret -= i
    i += 2

# while n > 0:
#     ret += n if n % 2 else -n
#     n -= 1

# while n > 0:
#     if n % 2:
#         ret += n
#     else:
#         ret -= n
#     n -= 1

print(f'结果为：{ret}')
