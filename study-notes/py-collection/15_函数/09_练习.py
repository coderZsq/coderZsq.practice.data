def test1():
    print('test1')
    return 666


def test2():
    print('test2-1')
    print(test1() + 111)
    print('test2-2')


def test3():
    print('test3-1')
    test2()
    print('test3-2')


def test4():
    print('test4-1')
    test3()
    print('test4-2')


test4()
