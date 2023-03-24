class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f'{self.__age}岁{self.__name}'


s = Student('MJ', 10)
print(s.__dict__)
print(s)
