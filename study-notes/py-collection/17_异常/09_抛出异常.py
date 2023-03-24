class Person:
    def __init__(self):
        self.__age = 1

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 1:  # 主动抛出异常
            raise ValueError('age不能小于1')

        if age > 120:  # 主动抛出异常
            raise ValueError('age不能大于120')

        self.__age = age

        # if age < 1:  # 主动抛出异常
        #     raise ValueError('age不能小于1')
        # elif age > 120:  # 主动抛出异常
        #     raise ValueError('age不能大于120')
        # else:
        #     self.__age = age


p1 = Person()

try:
    p1.age = -10
except ValueError as e:
    print('出现了异常', e.args[0])

print(p1.age)

# p2 = Person()
# p2.age = -10
# print(p2.age)  # 1
