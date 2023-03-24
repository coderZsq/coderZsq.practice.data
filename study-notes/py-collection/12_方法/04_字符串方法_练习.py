# 方法2
all_times = [0 for _ in range(10)]

for c in input('请输入数字：'):
    all_times[int(c)] += 1

for no, times in enumerate(all_times):
    print(f'{no}出现了{times}次')

# 方法1
# s = input('请输入数字：')
#
# for i in range(10):
#     print(f'{i}出现了{s.count(str(i))}次')
