class Animal:
    pass


class Dog(Animal):
    pass


class Cat(Animal):
    pass


print(Dog.__base__)
print(Cat.__base__)

d = Dog()
print(d.__class__.__base__)

print(Dog.__bases__)

print(Animal.__subclasses__())

