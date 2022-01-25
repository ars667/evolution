import pygame
import random
import math

# основные переменные
WIDTH = 800
HEIGHT = 480
FPS = 60
number_of_food = 10 #*2
number_of_men = 0
speed = 2

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (185, 185, 185)


# Создаем игру и окно

class food(pygame.sprite.Sprite):  # описание пищи
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


class man(pygame.sprite.Sprite):  # описание существа
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

        self.rect.x += dx * speed
        self.rect.y += dy * speed


class Player1(pygame.sprite.Sprite):  # описание существа
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

        self.rect.x += dx * speed
        self.rect.y += dy * speed


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("EVOLUTION")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
foods = pygame.sprite.Group()
player1 = Player1()
smh = man()

all_sprites.add(player1)
all_sprites.add(smh)
players.add(player1)
players.add(smh)
for i in range(number_of_food):
    m = food()
    m1 = food()
    all_sprites.add(m)
    foods.add(m)
    all_sprites.add(m1)
    foods.add(m1)
for i in range(number_of_men):
    man1 = man()
    all_sprites.add(man1)
    players.add(man1)

# Цикл игры
SIT = 0  # сытости существ
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
    if len(foods.sprites()) == 1:
        pygame.quit()
        print('СЫТОСТЬ СУЩЕСТВА 1 = ', SIT)
        print('СЫТОСТЬ СУЩЕСТВА 3 = ', SIT3)
    # Проверка, не съело ли существо еду
    hits1 = pygame.sprite.spritecollide(player1, foods, False)
    if hits1:
        SIT += 1

    hits3 = pygame.sprite.spritecollide(smh, foods, False)
    if hits3:
        SIT3 += 1

    hits = pygame.sprite.groupcollide(foods, players, True, False)
    if hits:
        best_food = foods.sprites()[0]
        for i in range(len(foods.sprites())):
            if math.sqrt((foods.sprites()[i].rect.x - smh.rect.x) ** 2 + (
                    foods.sprites()[i].rect.y - smh.rect.y) ** 2) < math.sqrt(
                (best_food.rect.x - smh.rect.x) ** 2 + (best_food.rect.y - smh.rect.y) ** 2) and foods.sprites()[
                i].rect.x != smh.rect.x and foods.sprites()[i].rect.y != smh.rect.x:
                best_food = foods.sprites()[i]
        m1 = best_food
        m = random.choice(foods.sprites())

    # Рендеринг

    screen.fill(GREY)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
