import turtle as t

# 设置画笔的大小
t.pensize(20)

# 隐藏方向箭头
t.hideturtle()

# 第1条边
t.pencolor('red')
t.forward(100)

# 第2条边
t.pencolor('green')
t.right(90)
t.forward(100)

# 第3条边
t.pencolor('blue')
t.right(90)
t.forward(100)

# 第4条边
t.pencolor('orange')
t.right(90)
t.forward(100)

t.mainloop()