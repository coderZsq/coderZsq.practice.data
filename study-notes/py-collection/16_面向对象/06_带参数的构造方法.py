class Dog:
    def __init__(self, name=None, breed=None, age=None):
        self.name = name
        self.age = age
        self.breed = breed

    def eat(self, food):
        print(f'【{self.age}岁{self.breed}{self.name}】吃了{food}')


d = Dog('宝哥', '柴犬', 10)
# 【10岁柴犬宝哥】吃了巧克力
d.eat('巧克力')

d2 = Dog('宝哥2', '柴犬2', None)
d2.eat('巧克力2')

d3 = Dog('宝哥3', '柴犬3')
d3.eat('巧克力3')

d4 = Dog()
d4.eat('巧克力4')
