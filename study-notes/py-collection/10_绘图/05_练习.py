import turtle as t

t.hideturtle()

# 半径
radius = 150
x = -30

# 右半圆
t.circle(radius, 180)
t.goto(0, 0)

# 把画笔抬起来
t.penup()
# 挪动位置
t.goto(x, 0)
# 把画笔放下去
t.pendown()

# 左半圆
t.circle(-radius, 180)
t.goto(x, 0)

t.mainloop()
