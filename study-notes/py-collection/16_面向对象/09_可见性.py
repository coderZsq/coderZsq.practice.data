class Student:
    def __init__(self):
        self.__name = None
        self.__age = None

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


s = Student()
s.set_name('MJ')
s.set_age(-500)
print(s.get_name())
print(s.get_age())
print(s)

# 目的：允许外界修改对象内部的属性，但是不允许它乱改
# 1.隐藏属性：让属性对外不可见
# 2.提供操作属性的方法：访问（读取）、修改
