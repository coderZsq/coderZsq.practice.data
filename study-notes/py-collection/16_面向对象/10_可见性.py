class Student:
    def __init__(self, name, age):
        self.__name = None
        self.__age = None
        self.set_name(name)
        self.set_age(age)

    def __str__(self):
        return f'{self.__age}岁{self.__name}'

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age if age > 0 else 1


s = Student('MJ', -10)
print(s.get_name())
print(s.get_age())
print(s)
