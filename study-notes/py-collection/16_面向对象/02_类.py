# 定义一个新的类
# 类的名字（类名）叫做Dog
class Dog:
    """狗"""
    pass


def run(dog: Dog):
    """
    让一只狗跑步
    :param dog: 狗
    """
    print(f'一只名字叫{dog.name}的{dog.age}岁{dog.breed}跑起来了！')


d1 = Dog()
d1.name = '宝哥'
d1.breed = '柴犬'
d1.age = 5
run(d1)
# 一只名字叫宝哥的5岁柴犬跑起来了！

d2 = Dog()
d2.name = '旺财'
d2.breed = '中华田园犬'
d2.age = 3
run(d2)
# 一只名字叫旺财的3岁中华田园犬跑起来了！

d3 = Dog()
d3.name = '拆哥'
d3.breed = '哈士奇'
d3.age = 4
run(d3)
# 一只名字叫拆哥的4岁哈士奇跑起来了！


class Cat:
    pass


c1 = Cat()
c2 = Cat()
print(type(c1))
