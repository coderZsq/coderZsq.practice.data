# 编写一个函数：可以向任意多个人打招呼
def hello(*names, title='Hi'):
    for n in names:
        print(f'{title}, {n}!')


hello('MJ', 'Jack', 'Rose', title='您好')

# def hello(title='Hi', *names):
#     for n in names:
#         print(f'{title}, {n}!')
#
#
# hello('哈罗', 'MJ', 'Jack', 'Rose')


# def hello(*names, title):
#     for n in names:
#         print(f'{title}, {n}!')
#
#
# hello('MJ', 'Jack', 'Rose', title='哈罗')

# def hello(title, *names):
#     for n in names:
#         print(f'{title}, {n}!')
#
#
# hello('哈罗', 'MJ', 'Jack', 'Rose')
