# 需求：
# 实时统计程序中一共有多少条狗
# 比如每创建一条狗，就打印：创建了第xx条狗
class Dog:
    count = 0

    def __init__(self, name):
        self.__name = name

        Dog.count += 1
        print(f'创建了第{Dog.count}条狗')


d1 = Dog('旺财')
d2 = Dog('宝哥')
d3 = Dog('拆哥')
d4 = Dog('拆哥')

# student_count = 0
# cat_count = 0
#
#
# class Student:
#     def __init__(self):
#         global student_count
#         student_count += 1
#
#
# class Cat:
#     def __init__(self):
#         global cat_count
#         cat_count += 1
#
#
# class Student:
#     count = 0
#
#     def __init__(self):
#         Student.count += 1
#
#
# class Cat:
#     count = 0
#
#     def __init__(self):
#         Cat.count += 1
