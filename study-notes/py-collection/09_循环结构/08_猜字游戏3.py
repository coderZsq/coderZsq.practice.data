# 定义一个0~1000之间的随机整数n为答案，提示用户输入一个整数k参与游戏猜答案
# 如果k != n，提示：猜错了，并要求重新输入
# 如果k == n，提示：经过x次猜测，恭喜回答正确，答案是n

import random as r

answer = r.randint(0, 1000)  # 正确答案
guess = int(input('请输入你的答案：'))  # 猜测的答案
times = 1  # 猜测的次数

# 如果回答错误，就提示再次输入答案
while guess != answer:
    print('猜大了' if guess > answer else '猜小了')

    guess = int(input('请输入你的答案：'))
    # 猜测的次数+1
    times += 1

# 回答正确
print(f'经过{times}次猜测，恭喜回答正确，答案是{answer}')
