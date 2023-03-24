import turtle as t


# def four_square(x, y, side):
#     def move(x1, y1):
#         t.penup()
#         t.goto(x1, y1)
#         t.pendown()
#
#     def square(side1):
#         for _ in range(4):
#             t.forward(side1)
#             t.right(90)
#
#     side /= 2
#     move(x, y)
#     square(side)
#
#     move(x + side, y)
#     square(side)
#
#     move(x, y - side)
#     square(side)
#
#     move(x + side, y - side)
#     square(side)

def four_square(x, y, side):
    # 内部函数
    def move(x1, y1):
        t.penup()
        t.goto(x1, y1)
        t.pendown()

    side /= 2

    # 内部函数
    def square():
        for _ in range(4):
            t.forward(side)
            t.right(90)

    move(x, y)
    square()

    move(x + side, y)
    square()

    move(x, y - side)
    square()

    move(x + side, y - side)
    square()


t.hideturtle()
four_square(-100, 100, 200)
t.mainloop()
