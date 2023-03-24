import turtle as t

t.color('red')
t.hideturtle()

t.begin_fill()
for _ in range(5):
    t.forward(200)
    t.right(144)
t.end_fill()

t.mainloop()
