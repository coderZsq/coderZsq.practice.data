k = 10


def test():
    # 这里的k是全局变量
    global k

    k = 20
    print('test')


print(f'k={k}')
test()
print(f'k={k}')
