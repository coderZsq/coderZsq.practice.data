class Animal:
    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")


class Dog(Animal):
    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):
    def fly(self):
        print("我会飞")

    def bark(self):
        print("叫的跟神一样...")
        super().bark()
        Dog.bark(self)
        print("!@#$%^&*")

xtq = XiaoTianQuan()
xtq.bark()