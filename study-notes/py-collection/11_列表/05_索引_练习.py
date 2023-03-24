import turtle as t
import random as r

# 待选的颜色
colors = [
    'red', 'blue', 'green', 'gray',
    'purple', 'orange', 'cyan', 'pink'
]
# 颜色的数量（只需要计算1次）
size = len(colors)

t.hideturtle()
t.pensize(10)

for _ in range(4):
    # 从colors列表中随机选择一个颜色
    i = r.randrange(size)
    t.color(colors[i])
    t.forward(100)
    t.right(90)

t.mainloop()
