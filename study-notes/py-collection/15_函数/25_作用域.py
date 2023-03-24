import turtle as t

# 全局变量
times = 4
angle = 90
side = 60


def square():
    for _ in range(times):
        t.forward(side)
        t.right(angle)


def test(a):
    # 局部变量
    b = 10
    print(times, angle, side)


square()
test()

t.mainloop()
