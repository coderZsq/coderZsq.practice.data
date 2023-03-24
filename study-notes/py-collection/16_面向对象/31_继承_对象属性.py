class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age


class Student(Person):
    def __init__(self, name, age, no):
        super().__init__(name, age)

        self.__no = no

    def show(self):
        print(f'no is {self.__no}')
        print(f'name is {self.name}')
        print(f'age is {self.age}')


s = Student('MJ', 18, 1)
s.show()
