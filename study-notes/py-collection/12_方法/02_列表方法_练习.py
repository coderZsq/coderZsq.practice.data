# 存放所有的汽车品牌
brands = []

while True:
    s = input('请输入汽车品牌：')

    if s == '0':  # 退出
        break

    if s in brands:  # 汽车品牌在列表里面
        continue

    # 将汽车品牌添加到列表中
    brands.append(s)

# 打印
print('-' * 30)  # 分隔线
print(f'一共{len(brands)}种汽车品牌：')
print(brands)

# while True:
#     s = input('请输入汽车品牌：')
#
#     if s == '0':  # 退出
#         break
#
#     if s not in brands:  # 汽车品牌不在列表里面
#         # 将汽车品牌添加到列表中
#         brands.append(s)
