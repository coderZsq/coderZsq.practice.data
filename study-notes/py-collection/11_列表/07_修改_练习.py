scores = [80, 96, 67, 54, 83]

while True:
    # 打印列表
    print(scores)
    # 修改分数
    scores[int(input('请输入索引：'))] = int(input('请输入分数：'))
    # 打印空行
    print()

# while True:
#     # 打印列表
#     print(scores)
#     # 提示输入
#     index = int(input('请输入索引：'))
#     score = int(input('请输入分数：'))
#     # 修改分数
#     scores[index] = score
#     # 打印空行
#     print()

