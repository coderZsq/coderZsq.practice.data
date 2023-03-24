def test3():
    print('test3 - 1')
    print(10 / 0)
    print('test3 - 2')


def test2():
    print('test2 - 1')
    test3()
    print('test2 - 2')


def test1():
    print('test1 - 1')

    try:
        test2()
    except:
        print('在test1函数中出现了异常')

    print('test1 - 2')


print(0)
test1()
print(4)


