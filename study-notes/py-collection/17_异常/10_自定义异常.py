class AgeError(Exception):
    """自定义的异常类型，表示age有问题"""
    def __str__(self):
        if len(self.args) == 1:
            return f'{self.args[0]}'
        return f'{self.args}'


class Person:
    def __init__(self):
        self.__age = 1

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 1:  # 主动抛出异常
            raise AgeError('age不能小于1', 66)

        if age > 120:  # 主动抛出异常
            raise AgeError('age不能大于120', 77)

        self.__age = age


try:
    p = Person()
    p.age = 300
    print(p.age)
except AgeError as e:
    print('出现了异常', e.args)
    print('出现了异常', e)





