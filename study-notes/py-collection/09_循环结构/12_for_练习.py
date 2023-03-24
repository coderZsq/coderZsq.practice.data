# 提示输入一个1~100之间的正整数n
# 如果输入错误，要求重新输入
# 如果输入正确，请打印以下计算结果（不准使用便捷的数学公式）


# 如果输入错误，要求重新输入
n = 0
while n < 1 or n > 100:
    n = int(input('请输入[1, 100]范围的整数：'))

# 1 + 2 + 3 + 4 + ... + n
ret = 0
for i in range(1, n + 1):
    ret += i
print(f'结果是{ret}')

# 1 – 2 + 3 – 4 + ... + n（所有的奇数相加，减去所有的偶数）
ret = 0
for i in range(1, n + 1):
    ret += i if i % 2 else -i
print(f'结果是{ret}')

# 1 + 3 + 5 + 7 + ... + n（所有的奇数相加）
ret = 0
for i in range(1, n + 1, 2):
    ret += i
print(f'结果是{ret}')

