class MusicPlayer(object):
    def __new__(cls, *args, **kwargs):
        print("创建对象, 分配空间")
        instance = super().__new__(cls)
        return instance

    def __init__(self):
        print("播放器初始化")


player = MusicPlayer()
print(player)
