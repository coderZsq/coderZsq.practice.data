# 定义一个0~1000之间的随机整数n为答案，提示用户输入一个整数k参与游戏猜答案
# 如果k != n，提示：猜错了，并要求重新输入
# 如果k == n，提示：经过x次猜测，恭喜回答正确，答案是n

import random as r

left = 0  # 左边界
right = 1000  # 右边界
answer = r.randint(left, right)  # 正确答案
guess = -1  # 猜测的答案
times = 0  # 猜测的次数

# 如果回答错误，就提示再次输入答案
while guess != answer:
    if guess > answer:  # 猜大了
        right = min(guess - 1, right)
    else:  # 猜小了
        left = max(guess + 1, left)
    guess = int(input(f'请输入[{left}, {right}]范围内的整数：'))
    # 猜测的次数+1
    times += 1

# 回答正确
print(f'经过{times}次猜测，恭喜回答正确，答案是{answer}')
