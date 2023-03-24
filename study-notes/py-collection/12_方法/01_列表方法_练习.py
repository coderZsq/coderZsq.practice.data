import turtle as t
import random as r

# 待选的颜色
colors = [
    'red', 'blue', 'green', 'gray',
    'purple', 'orange', 'cyan', 'pink'
]

t.hideturtle()
t.pensize(10)

t.begin_fill()
for _ in range(4):
    # 从colors列表中随机选择一个颜色
    i = r.randrange(len(colors))
    # 删除并返回颜色
    t.pencolor(colors.pop(i))

    t.forward(100)
    t.right(90)
# 设置填充色
t.fillcolor(colors[r.randrange(len(colors))])
t.end_fill()

t.mainloop()

# # 设置填充色
# i = r.randrange(len(colors))
# t.fillcolor(colors.pop(i))
# for _ in range(4):
#     # 从colors列表中随机选择一个颜色
#     i = r.randrange(len(colors))
#     # 删除并返回颜色
#     t.pencolor(colors.pop(i))
#
#     t.forward(100)
#     t.right(90)

# t.begin_fill()
# for _ in range(4):
#     # 从colors列表中随机选择一个颜色
#     i = r.randrange(len(colors))
#     t.color(colors[i])
#     # 删除颜色
#     colors.pop(i)
#     t.forward(100)
#     t.right(90)
# t.fillcolor(colors[r.randrange(len(colors))])
# t.end_fill()
