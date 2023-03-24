class Student:
    def __init__(self):
        self.__name = None
        self.__age = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        del self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age if age > 0 else 1

    @age.deleter
    def age(self):
        del self.__age


s = Student()
s.name = 'MJ'
s.age = 10
print(s.name)
print(s.age)
print(s.__dict__)

# s.delete_name()
del s.name
print(s.__dict__)

# s.delete_age()
del s.age
print(s.__dict__)

# s.set_name('MJ')
# s.set_age(10)
# print(s.get_name())
# print(s.get_age())
