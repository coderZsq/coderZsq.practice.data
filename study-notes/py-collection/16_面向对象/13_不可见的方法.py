class Dog:
    def __init__(self, name):
        self.__name = name

    def run(self):
        print('run', self.__name)

    def __sleep(self):
        print('sleep', self.__name)


s = Dog('旺财')
# run 旺财
s.run()

# sleep 旺财
s._Dog__sleep()

# s.__sleep()

# dir函数：所有可用的属性名、方法名
print(dir(s))
