import turtle as t
import random as r

# 设置画笔的大小
t.pensize(20)
# 隐藏方向箭头
t.hideturtle()
t.colormode(255)

# 第1条边
t.pencolor(
    r.randint(0, 255),
    r.randint(0, 255),
    r.randint(0, 255)
)
t.forward(100)

# 第2条边
t.pencolor(
    r.randint(0, 255),
    r.randint(0, 255),
    r.randint(0, 255)
)
t.right(90)
t.forward(100)

# 第3条边
t.pencolor(
    r.randint(0, 255),
    r.randint(0, 255),
    r.randint(0, 255)
)
t.right(90)
t.forward(100)

# 第4条边
t.pencolor(
    r.randint(0, 255),
    r.randint(0, 255),
    r.randint(0, 255)
)
t.right(90)
t.forward(100)

t.mainloop()