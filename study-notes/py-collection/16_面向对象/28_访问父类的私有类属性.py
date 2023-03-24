class Person:
    __count = 10

    @classmethod
    def get_count(cls):
        # cls._Person__count
        return cls.__count


class Student(Person):
    @classmethod
    def show(cls):
        # 访问父类中的私有属性count
        # print(cls._Person__count)
        print(cls.get_count())


Student.show()
