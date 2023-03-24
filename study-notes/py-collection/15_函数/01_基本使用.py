import turtle as t

t.hideturtle()

# 画第1个正方形
t.penup()
t.goto(120, 60)
t.pendown()
for _ in range(4):
    t.forward(50)
    t.right(90)

# 画第2个正方形
t.penup()
t.goto(-75, 98)
t.pendown()
for _ in range(4):
    t.forward(50)
    t.right(90)

# 画第3个正方形
t.penup()
t.goto(-86, -110)
t.pendown()
for _ in range(4):
    t.forward(50)
    t.right(90)

# 画第4个正方形
t.penup()
t.goto(53, -69)
t.pendown()
for _ in range(4):
    t.forward(50)
    t.right(90)

t.mainloop()
