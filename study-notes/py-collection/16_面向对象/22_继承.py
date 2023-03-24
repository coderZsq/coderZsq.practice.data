# class Animal:
#     def sleep(self):
#         print(self, 'sleep')
#
#     def run(self):
#         print(self, 'run')
#
#
# class Dog(Animal):
#     def wag_tail(self):
#         print(self, 'wag_tail')
#
#
# class Cat(Animal):
#     def catch_mouse(self):
#         print(self, 'catch_mouse')
#

class Animal:
    def sleep(self):
        print(self, 'sleep')

    def run(self):
        print(self, 'run')


class Dog(Animal):
    pass


class Cat(Animal):
    pass


d = Dog()
d.sleep()
d.run()

print('-' * 30)

c = Cat()
c.sleep()
c.run()

