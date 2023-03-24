import random as r

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

# no是随机数（索引）
# times是随机数（索引）出现的次数
for no, times in enumerate(all_times):
    print(f'{no}出现了{times}次')

# 从小到大打印随机数
for no, times in enumerate(all_times):
    print(f'{no} ' * times, end='')

# for no, times in enumerate(all_times):
#     for _ in range(times):
#         print(no, end=' ')
