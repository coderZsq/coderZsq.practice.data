import pygame

pygame.init()

screen = pygame.display.set_mode((480, 700))

bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))

hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 500))

pygame.display.update()

clock = pygame.time.Clock()

i = 0

while True:
    clock.tick(1)
    i += 1
    print(i)
    pass

pygame.quit()
