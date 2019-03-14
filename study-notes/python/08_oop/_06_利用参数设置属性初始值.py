class Cat:
    def __init__(self, new_name):
        print("这是一个初始化方法")
        # self.name = "Tom"
        self.name = new_name

    def eat(self):
        print("%s 爱吃鱼" % self.name)


tom = Cat("Tom")
print(tom.name)

lazy_cat = Cat("大懒猫")
lazy_cat.eat()
