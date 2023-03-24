class Dog:
    def run(self):
        print(f'【{self.age}岁{self.breed}{self.name}】跑起来了')


d1 = Dog()
d1.name = '宝哥'
d1.breed = '柴犬'
d1.age = 5
# 【5岁柴犬宝哥】跑起来了
d1.run()

d2 = Dog()
d2.name = '旺财'
d2.breed = '中华田园犬'
d2.age = 3
# 【3岁中华田园犬旺财】跑起来了
d2.run()

d3 = Dog()
d3.name = '拆哥'
d3.breed = '哈士奇'
d3.age = 4
# 【4岁哈士奇拆哥】跑起来了
d3.run()
