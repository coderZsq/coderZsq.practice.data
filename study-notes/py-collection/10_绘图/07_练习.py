import turtle as t
import random as r

t.speed(0)
t.pensize(10)
t.colormode(255)
t.hideturtle()

for i in range(5, 0, -1):
    # 设置画笔颜色
    t.color(
        r.randint(0, 255),
        r.randint(0, 255),
        r.randint(0, 255)
    )

    # 半径
    radius = 30 * i

    # 修改一下起点
    t.penup()
    t.sety(-radius)
    t.pendown()

    # 画圆
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

t.mainloop()
