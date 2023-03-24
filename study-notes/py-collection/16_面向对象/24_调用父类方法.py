class Animal:
    def run(self):
        print(id(self), 'Animal run')


class Dog(Animal):
    def run(self):
        print(id(self), 'Dog run')


class RobotDog(Dog):
    def run(self):
        print(id(self), 'RobotDog run')

    def fly(self):
        # 调用RobotDog的run方法
        self.run()

        # 调用Dog的run方法
        Dog.run(self)
        RobotDog.__base__.run(self)
        super(RobotDog, self).run()
        super().run()

        # 调用Animal的run方法
        Animal.run(self)
        Dog.__base__.run(self)
        super(Dog, self).run()

        print(id(self), 'RobotDog fly')


rd = RobotDog()
rd.fly()
