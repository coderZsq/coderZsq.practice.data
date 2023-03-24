class Dog:
    def __init__(self):
        # 声明并初始化属性（成员变量、实例变量）
        self.name = None
        self.age = None
        self.breed = None

    def run(self):
        print(f'【{self.age}岁{self.breed}{self.name}】跑起来了')


d = Dog()
d.name = '宝哥'
d.breed = '柴犬'
d.age = 10
d.run()

# 类的作用？
# 描述、模拟一种事物类型

# 存在的问题
# 1.从class代码里面看不出有哪些属性
# 2.属性名没有任何提示
# 3.不同的对象可以拥有不同数量的属性
# 4.在方法中访问对象属性时会有警告
