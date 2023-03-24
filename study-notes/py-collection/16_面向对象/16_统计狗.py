# 需求：
# 实时统计程序中一共有多少条狗
# 比如每创建一条狗，就打印：创建了第xx条狗

count = 0


class Dog:
    def __init__(self, name):
        self.__name = name

        global count
        count += 1
        print(f'创建了第{count}条狗')


d1 = Dog('旺财')
d2 = Dog('宝哥')
d3 = Dog('拆哥')
d4 = Dog('拆哥')
