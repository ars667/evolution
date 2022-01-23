import pygame
import random
import math

WIDTH = 800
HEIGHT = 480
FPS = 10
number_of_food = 10

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (185, 185, 185)


# Создаем игру и окно

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT)
        self.speedy = 0

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(HEIGHT - self.rect.height)
            self.speedy = random.randrange(1, 8)


class SMH(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image = pygame.image.load(
            'sprite\man.png')
        self.image.set_colorkey(WHITE)
        # self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(HEIGHT - self.rect.height)

    def update(self):
        dx = 0
        dy = 0
        if self.rect.left < m1.rect.left and self.rect.right > m1.rect.right:
            dx = 0
        elif self.rect.left < m1.rect.left:
            dx = 1
        elif self.rect.right > m1.rect.right:
            dx = -1

        if self.rect.top < m1.rect.top and self.rect.bottom > m1.rect.bottom:
            dy = 0
        elif self.rect.top < m1.rect.top:
            dy = 1
        elif self.rect.bottom > m1.rect.bottom:
            dy = -1

        self.rect.x += dx * 10
        self.rect.y += dy * 10


class Player1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        # self.image = pygame.image.load(
        # 'военный2.png').convert_alpha()
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(HEIGHT - self.rect.height)

    def update(self):
        dx = 0
        dy = 0
        if self.rect.left < m.rect.left and self.rect.right > m.rect.right:
            dx = 0
        elif self.rect.left < m.rect.left:
            dx = 1
        elif self.rect.right > m.rect.right:
            dx = -1

        if self.rect.top < m.rect.top and self.rect.bottom > m.rect.bottom:
            dy = 0
        elif self.rect.top < m.rect.top:
            dy = 1
        elif self.rect.bottom > m.rect.bottom:
            dy = -1

        self.rect.x += dx * 10
        self.rect.y += dy * 10


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("EVOLUTION")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
mobs = pygame.sprite.Group()
player1 = Player1()
smh = SMH()

all_sprites.add(player1)
all_sprites.add(smh)
players.add(player1)
players.add(smh)
for i in range(number_of_food):
    m = Mob()
    m1 = Mob()
    all_sprites.add(m)
    mobs.add(m)
    all_sprites.add(m1)
    mobs.add(m1)
# Цикл игры
SIT = 0
SIT2 = 0
SIT3 = 0
running = True
while running:

    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update()

    # Проверка, не съело ли существо еду
    hits1 = pygame.sprite.spritecollide(player1, mobs, False)
    if hits1:
        SIT += 1
        print('СЫТОСТЬ СУЩЕСТВА 1 = ', SIT)

    hits3 = pygame.sprite.spritecollide(smh, mobs, False)
    if hits3:
        SIT3 += 1
        print('СЫТОСТЬ СУЩЕСТВА 3 = ', SIT3)
    hits = pygame.sprite.groupcollide(mobs, players, True, False)
    if hits:
        best_food = mobs.sprites()[1]
        for i in range(len(mobs.sprites())):
            if math.sqrt((mobs.sprites()[i].rect.x - smh.rect.x) ** 2 + (
                    mobs.sprites()[i].rect.y - smh.rect.y) ** 2) < math.sqrt(
                (best_food.rect.x - smh.rect.x) ** 2 + (best_food.rect.y - smh.rect.y) ** 2) and mobs.sprites()[
                i].rect.x != smh.rect.x and mobs.sprites()[i].rect.y != smh.rect.x:
                best_food = mobs.sprites()[i]
        m1 = best_food
        m = random.choice(mobs.sprites())
    # for hit in hits:
    # SIT += 1
    # print(SIT)
    #   p1 = player1
    #  p2 = player2
    # all_sprites.add(p1)
    # players.add(p1)
    # all_sprites.add(p2)
    # players.add(p2)
    # Рендеринг

    screen.fill(GREY)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
