# 需求：根据创建顺序，给每一条狗设置一个编号，比如，如果是第6条狗，那么它的编号就是6
class Dog:
    __count = 0

    def __init__(self, name):
        self.__name = name
        Dog.__count += 1
        self.__no = Dog.__count

    def __str__(self):
        return f'{self.__no}_{self.__name}'


d1 = Dog('旺财')
print(d1)

d2 = Dog('拆哥')
print(d2)

Dog.count = 10

for _ in range(3):
    Dog('66')

d3 = Dog('宝哥')
print(d3)
