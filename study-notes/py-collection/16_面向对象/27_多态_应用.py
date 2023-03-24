class Animal:
    def run(self):
        print('Animal run')


class Dog(Animal):
    def run(self):
        print('Dog run')


class Cat(Animal):
    def run(self):
        print('Cat run')


class Pig(Animal):
    def run(self):
        print('Pig run')


def run_animal(obj: Animal, times: int):
    for _ in range(times):
        obj.run()


run_animal(Dog(), 3)
run_animal(Cat(), 2)
run_animal(Pig(), 2)

# def run_dog(obj: Dog, times: int):
#     for _ in range(times):
#         obj.run()
#
#
# def run_cat(obj: Cat, times: int):
#     for _ in range(times):
#         obj.run()
#
#
# def run_pig(obj: Pig, times: int):
#     for _ in range(times):
#         obj.run()
#
#
# run_dog(Dog(), 4)
# run_cat(Cat(), 3)
