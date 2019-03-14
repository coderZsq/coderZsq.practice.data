class Cat:
    def eat(self):
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 要喝水" % self.name)


tom = Cat()
tom.name = "Tom"
tom.eat()
tom.drink()
print(tom)

lazy_cat = Cat()
lazy_cat.name = "大懒猫"
lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)
