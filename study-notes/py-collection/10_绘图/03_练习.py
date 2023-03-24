import turtle as t

t.color('green')
# 设置方向箭头的图案
t.shape('square')
# 盖章（将方向箭头的图案印上去）
t.stamp()

for i in range(50):
    t.forward(50 + i * 5)
    t.right(60)
    # 盖章（将方向箭头的图案印上去）
    t.stamp()

t.mainloop()
