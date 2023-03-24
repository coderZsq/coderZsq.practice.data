class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f'{self.__age}岁{self.__name}'


s = Student('MJ', 10)
s.__name = 'Jack'
s.__age = 20
print(s.__name)
print(s.__age)
