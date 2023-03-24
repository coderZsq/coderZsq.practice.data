import turtle as t

t.hideturtle()
t.pensize(5)
t.pencolor('green')

t.fillcolor('red')
t.begin_fill()
# 第1条边
t.forward(100)
# 第2条边
t.right(90)
t.forward(100)
t.end_fill()

t.fillcolor('blue')
t.begin_fill()
# 第3条边
t.right(90)
t.forward(100)
# 第4条边
t.right(90)
t.forward(100)
t.end_fill()

t.mainloop()