# n = 0
# ret = 0
#
# while n != -1:
#     n = int(input('请输入整数：'))
#     if n > 0:  # 正整数
#         ret += n
#
# print(f'正整数的和是{ret}')

# ret = 0
#
# while True:
#     n = int(input('请输入整数：'))
#     if n > 0:
#         ret += n
#     elif n == -1:
#         break
#
# print(f'正整数的和是{ret}')

ret = 0

while True:
    n = int(input('请输入整数：'))

    if n == -1:
        break
    elif n <= 0:
        continue

    ret += n

print(f'正整数的和是{ret}')
