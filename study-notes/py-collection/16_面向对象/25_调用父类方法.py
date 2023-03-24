class Animal:
    def run(self):
        print(id(self), 'Animal run')


class Dog(Animal):
    def run(self):
        # 调用父类的run方法
        # super(Dog, self).run()
        super().run()
        print(id(self), 'Dog run')


class RobotDog(Dog):
    def run(self):
        # 调用父类的run方法
        # super(RobotDog, self).run()
        super().run()
        print(id(self), 'RobotDog run')


rd = RobotDog()
rd.run()
