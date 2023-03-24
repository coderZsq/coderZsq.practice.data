class Animal:
    def run(self):
        print('Animal run')


class Dog(Animal):
    def run(self):
        print('Dog run')


class Cat(Animal):
    def run(self):
        print('Cat run')


def test(obj: Animal):
    obj.run()


a = Animal()
d = Dog()
c = Cat()

test(a)
test(d)
test(c)

# test(10)
# test('45354')
