import random as r

# 方法2
# 随机数的范围
edge = 10
# 随机数的数量
size = 20

# 生成随机数
nos = [r.randrange(edge) for _ in range(size)]

# 统计每一个随机数的出现次数
all_times = [0 for _ in range(edge)]
for no in nos:
    all_times[no] += 1

# 打印
print(nos)
for no, times in enumerate(all_times):
    print(f'{no}出现了{times}次')

# all_times[no]就代表随机数no的出现次数
# 比如all_times[0]就代表随机数0的出现次数
# 比如all_times[9]就代表随机数9的出现次数

# 方法1
# 统计每一个随机数的出现次数
# nos = [0 for _ in range(20)]
# for i in range(len(nos)):
#     nos[i] = r.randrange(10)

# times0 = 0
# times1 = 0
# times2 = 0
# times3 = 0
# times4 = 0
# times5 = 0
# times6 = 0
# times7 = 0
# times8 = 0
# times9 = 0
# for no in nos:
#     if no == 0:
#         times0 += 1
#     elif no == 1:
#         times1 += 1
#     elif no == 2:
#         times2 += 1
#     elif no == 3:
#         times3 += 1
#     elif no == 4:
#         times4 += 1
#     elif no == 5:
#         times5 += 1
#     elif no == 6:
#         times6 += 1
#     elif no == 7:
#         times7 += 1
#     elif no == 8:
#         times8 += 1
#     elif no == 9:
#         times9 += 1
#
# print(nos)
# print(f'0出现了{times0}次')
# print(f'1出现了{times1}次')
# print(f'2出现了{times2}次')
# print(f'3出现了{times3}次')
# print(f'4出现了{times4}次')
# print(f'5出现了{times5}次')
# print(f'6出现了{times6}次')
# print(f'7出现了{times7}次')
# print(f'8出现了{times8}次')
# print(f'9出现了{times9}次')
