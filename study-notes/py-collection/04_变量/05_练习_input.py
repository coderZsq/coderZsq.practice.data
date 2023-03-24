import turtle as t

side = int(input('请输入正方形的边长：'))
angle = 90

t.forward(side)
t.right(angle)
t.forward(side)
t.right(angle)
t.forward(side)
t.right(angle)
t.forward(side)

t.mainloop()