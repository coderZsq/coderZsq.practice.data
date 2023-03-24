class Person:
    def __init__(self):
        print('Person init')
        # 初始化属性
        self.name = 'MJ'
        self.age = 18


class Student(Person):
    def __init__(self):
        super().__init__()

        print('Student init')
        self.no = 9


s = Student()
print(s.__dict__)
