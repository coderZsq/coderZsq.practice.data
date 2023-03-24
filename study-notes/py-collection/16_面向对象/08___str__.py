class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'【{self.age}岁{self.name}】'

    def run(self):
        print(f'{self}跑起来了')

    def eat(self, food):
        print(f'{self}吃了{food}')


d = Dog('宝哥', 5)
print(d)

# print(str(d))
# print(d)

# print(d.age)
# print(d.name)

# print(d.__dict__)

# print(f'{d.age}岁{d.name}')

# 5岁宝哥跑起来了
d.run()

# 5岁宝哥吃了巧克力
d.eat('巧克力')

