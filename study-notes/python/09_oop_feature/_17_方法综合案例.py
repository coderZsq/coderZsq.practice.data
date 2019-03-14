class Game(object):
    top_score = 0

    def __init__(self, play_name):
        self.play_name = play_name

    @staticmethod
    def show_help():
        print("帮助信息: 让僵尸进入大门")

    @classmethod
    def show_top_score(cls):
        print("历史记录 %d" % cls.top_score)

    def start_game(self):
        print("%s 开始游戏啦..." % self.play_name)


Game.show_help()
Game.show_top_score()
game = Game("小明")
game.start_game()
