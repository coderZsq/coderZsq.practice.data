import turtle as t


# 定义一个画正方形的函数
def draw_square(side):
    for _ in range(4):
        t.forward(side)
        t.right(90)


# 定义一个挪动位置的函数
def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


# 定义一个挪动位置+画正方形的函数
def move_square(x, y, side):
    move(x, y)
    draw_square(side)


t.hideturtle()

# 画第1个正方形
move_square(120, 60, 100)

# 画第2个正方形
move_square(-75, 98, 80)

# 画第3个正方形
move_square(-86, -110, 50)

# 画第4个正方形
move_square(53, -69, 60)

t.mainloop()
