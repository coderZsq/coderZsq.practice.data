import turtle as t


# 挪动位置+画圆
def move_circle(x, y, radius):
    # 挪动到(x, y)位置
    t.penup()
    t.goto(x, y)
    t.pendown()

    # 画1个半径为radius的圆
    t.circle(radius)


# move_circle(50, 60, 70)
s = [50, 60, 70]
move_circle(*s)
# move_circle(s[0], s[1], s[2])


t.mainloop()
