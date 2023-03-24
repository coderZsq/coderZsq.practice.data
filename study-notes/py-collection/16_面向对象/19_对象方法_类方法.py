class Dog:
    def test1(self, text):
        print('对象方法', id(self), text)

    @classmethod
    def test2(cls, text):
        print('类方法', id(cls), text)


d1 = Dog()
d2 = Dog()

# 对象方法
d1.test1('d1')
Dog.test1(d1, 'Dog')
d1.__class__.test1(d1, 'd1.__class__')
d2.__class__.test1(d1, 'd2.__class__')

print('-' * 30)

d2.test1('d2')
Dog.test1(d2, 'Dog')
d1.__class__.test1(d2, 'd1.__class__')
d2.__class__.test1(d2, 'd2.__class__')

print('-' * 30)

# 类方法
Dog.test2('Dog')
d1.__class__.test2('d1.__class__')
d2.__class__.test2('d2.__class__')
d1.test2('d1')
d2.test2('d2')
