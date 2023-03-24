import turtle as t


def move_circle(*, x=0, y=0, radius=50):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(radius)


move_circle(x=50, y=60, radius=70)


t.mainloop()
