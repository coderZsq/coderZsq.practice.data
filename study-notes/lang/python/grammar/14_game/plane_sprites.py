import random
import pygame

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
FRAME_PER_SEC = 60


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, *args):
        self.rect.y += self.speed


class Background(GameSprite):
    def __init__(self, is_alt=False):
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self, *args):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height
        pass


class Enemy(GameSprite):
    def __init__(self):
        super().__init__("./images/enemy1.png")
        self.speed = random.randint(3, 5)
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self, *args):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            print("飞出屏幕, 需要从精灵组删除...")
            self.kill()

    def __del__(self):
        print("敌机挂了 %s" % self.rect)


class Hero(GameSprite):
    def __init__(self):
        super().__init__("./images/me1.png", 0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.bullets = pygame.sprite.Group()

    def update(self, *args):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        print("发射子弹...")
        for i in (0, 1, 2):
            bullet = Bullet()
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            self.bullets.add(bullet)


class Bullet(GameSprite):
    def __init__(self):
        super().__init__("./images/bullet1.png", -8.5)

    def update(self, *args):
        super().update()
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("子弹被销毁...")
