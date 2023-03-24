import turtle as t

t.hideturtle()
t.pensize(5)
t.pencolor('blue')

# 半圆
t.fillcolor('red')
t.begin_fill()
t.circle(100, 180, 2)
t.end_fill()

# 半圆
t.fillcolor('green')
t.begin_fill()
t.circle(100, 180, 2)
t.end_fill()

t.mainloop()