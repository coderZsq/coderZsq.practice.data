class Dog:
    def test1(self, text):
        print('对象方法', id(self), text)

    @classmethod
    def test2(cls, text):
        print('类方法', id(cls), text)

    @staticmethod
    def test3(text):
        print('静态方法', text)


def test4(text):
    print('普通函数', text)


d = Dog()

# 对象方法
d.test1('d')
Dog.test1(d, 'Dog')
d.__class__.test1(d, 'd.__class__')

# 类方法
Dog.test2('Dog')
d.__class__.test2('d.__class__')
d.test2('Dog')

# 静态方法
d.test3('d')
Dog.test3('Dog')
d.__class__.test3('d.__class__')

# 普通函数
test4('777')
