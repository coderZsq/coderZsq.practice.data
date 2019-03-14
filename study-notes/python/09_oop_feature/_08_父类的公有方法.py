class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("私有方法 %d %d" % (self.num1, self.__num2))

    def test(self):
        print("父类的公有方法 %d" % self.__num2)
        self.__test()


class B(A):
    def demo(self):
        print("子类方法 %d" % self.num1)
        self.test()
        pass


b = B()
print(b)
b.demo()
