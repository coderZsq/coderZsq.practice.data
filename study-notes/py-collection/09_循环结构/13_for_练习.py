high = 0  # 初始值要比所有分数都低
low = 100  # 初始值要比所有分数都高

for i in range(1, 6):
    score = int(input(f'请输入第{i}位学员的分数：'))

    high = max(high, score)
    # if score > high:  # 找到了一个更高的分数
    #     high = score

    low = min(low, score)
    # if score < low:  # 找到了一个更低的分数
    #     low = score

print(f'最高分是：{high}，最低分是：{low}')
