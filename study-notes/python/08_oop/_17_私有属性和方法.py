class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def secret(self):
        print("%s 的年龄是 %d" % (self.name, self.__age))


xiaofang = Women("小芳")
xiaofang.secret()