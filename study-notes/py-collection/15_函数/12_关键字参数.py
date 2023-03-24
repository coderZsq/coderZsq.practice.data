import turtle as t


# 挪动位置+画圆
def move_circle(x=0, y=0, radius=50):
    # 挪动到(x, y)位置
    t.penup()
    t.goto(x, y)
    t.pendown()

    # 画1个半径为radius的圆
    t.circle(radius)


# 等价于move_circle(100, 0, 50)
move_circle(100)

move_circle(radius=100)

t.mainloop()
