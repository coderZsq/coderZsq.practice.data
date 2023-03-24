# 存放所有学员的分数
scores = [0 for _ in range(4)]

# 将所有学员的分数存放到scores列表中
for i in range(len(scores)):
    scores[i] = int(input(f'请输入第{i + 1}个学员的分数：'))

# 打印
print(f'最高分是：{max(scores)}，最低分是：{min(scores)}')
