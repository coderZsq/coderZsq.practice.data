class Dog:
    # 统计所有Dog实例对象的数量
    __count = 0

    def __init__(self, name):
        self.__name = name
        # Dog实例对象的数量+1
        self.__class__.__count += 1

    def __str__(self):
        return self.__name

    def run(self):
        print(self, 'run')

    def sleep(self):
        print(self, 'sleep')

    @classmethod
    def get_count(cls):
        return cls.__count

    @staticmethod
    def get_avg_weight():
        return 10


print(Dog.get_avg_weight())

# d1 = Dog('旺财')
# print(d1.get_avg_weight())

# d1.run()
# d1.sleep()
#
# d2 = Dog('宝哥')
# d2.run()
# d2.sleep()

print(Dog.get_count())

# print(d1.get_count())
# print(d2.get_count())
