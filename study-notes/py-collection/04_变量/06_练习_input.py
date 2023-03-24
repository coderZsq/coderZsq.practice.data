import turtle as t

# side = int(t.textinput('请输入', '正方形的边长'))
side = t.numinput('请输入', '正方形的边长')
angle = 90

t.forward(side)
t.right(angle)
t.forward(side)
t.right(angle)
t.forward(side)
t.right(angle)
t.forward(side)

t.mainloop()