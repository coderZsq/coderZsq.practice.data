def hello():
    """打印3次hello"""
    print('hello')
    print('hello')
    print('hello')


def avg(a: float, b: float) -> float:
    """
    计算2个数值的平均值
    :param a: 第1个数值
    :param b: 第2个数值
    :return: 平均值
    """
    return (a + b) / 2


# hello()
# print(avg(10, 30))

# print(avg.__doc__)
# help(avg)
print(avg.__annotations__)
