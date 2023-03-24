# 定义一个0~1000之间的随机整数n为答案，提示用户输入一个整数k参与游戏猜答案
# 如果k != n，提示：猜错了，并要求重新输入
# 如果k == n，提示：经过x次猜测，恭喜回答正确，答案是n

import random as r

n = r.randint(0, 1000)  # 正确答案
k = -1  # 猜测的答案
x = 0  # 猜测的次数

# 如果回答错误，就提示再次输入答案
while k != n:
    if x:  # 已经至少猜测过1次
        print('猜大了' if k > n else '猜小了')

        # print('猜大了') if k > n else print('猜小了')

        # if k > n:
        #     print('猜大了')
        # else:
        #     print('猜小了')

    k = int(input('请输入你的答案：'))
    # 猜测的次数+1
    x += 1

# 回答正确
print(f'经过{x}次猜测，恭喜回答正确，答案是{n}')
