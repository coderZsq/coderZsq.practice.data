class Dog:
    def info(self):
        """返回狗的具体信息"""
        return f'【{self.age}岁{self.breed}{self.name}】'

    def run(self):
        """跑步"""
        print(f'{self.info()}跑起来了')

    def eat(self, food):
        """
        吃东西
        :param food: 食物
        """
        print(f'{self.info()}吃了{food}')


d1 = Dog()
d1.name = '宝哥'
d1.breed = '柴犬'
d1.age = 5
# 【5岁柴犬宝哥】跑起来了
d1.run()
# 【5岁柴犬宝哥】吃了花生米
d1.eat('花生米')

d2 = Dog()
d2.name = '旺财'
d2.breed = '中华田园犬'
d2.age = 3
# 【3岁中华田园犬旺财】跑起来了
d2.run()
# 【3岁中华田园犬旺财】吃了巧克力
d2.eat('巧克力')
