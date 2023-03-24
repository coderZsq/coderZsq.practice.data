# 编写一个函数：可以向任意多个人打招呼
def hello(*names):
    for n in names:
        print(f'Hi, {n}!')


hello('MJ', 'Jack', 'Rose', '小码哥')
hello('MJ', 'Jack', 'Rose')
hello('MJ', 'Jack')
hello('MJ')
hello()

# hello('MJ', 'Jack', 'Rose', '小码哥', 'Michael', 'Jim')

# hello(['MJ', 'Jack', 'Rose', '小码哥', 'Michael'])
# hello(('MJ', 'Jack', 'Rose', '小码哥', 'Michael'))
