class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed


d1 = Dog('宝哥', 5, '柴犬')
print(d1.__dict__)

print('-' * 30)

d2 = Dog('旺财', 3, '土狗')
d2.weight = 10
print(d2.__dict__)
