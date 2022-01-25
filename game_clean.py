import pygame
import random
import math

width = 800
height = 480
FPS = 60
number_of_food = 12
speed = 4
daynight = 0

white = (255, 255, 255)
black = (0, 0, 0)
red = (205, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (195, 195, 195)


class food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, width)
        self.rect.y = random.randrange(0, height)


class man(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image = pygame.image.load('sprite\man.png')
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(height - self.rect.height)

    def update(self):
        dx = 0
        dy = 0

        if len(foods.sprites()) == 0:
            dx = 0
        elif self.rect.left < m.rect.left and self.rect.right > m.rect.right:
            dx = 0
        elif self.rect.left < m.rect.left:
            dx = 1
        elif self.rect.right > m.rect.right:
            dx = -1

        if len(foods.sprites()) == 0:
            dy = 0
        elif self.rect.top < m.rect.top and self.rect.bottom > m.rect.bottom:
            dy = 0
        elif self.rect.top < m.rect.top:
            dy = 1
        elif self.rect.bottom > m.rect.bottom:
            dy = -1

        self.rect.x += dx * speed
        self.rect.y += dy * speed


pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("evolution")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
foods = pygame.sprite.Group()
man = man()
all_sprites.add(man)
players.add(man)
for i in range(number_of_food):
    m = food()
    all_sprites.add(m)
    foods.add(m)
best_food = foods.sprites()[0]
for i in range(len(foods.sprites())):
    if math.sqrt((foods.sprites()[i].rect.x - man.rect.x) ** 2 + (
            foods.sprites()[i].rect.y - man.rect.y) ** 2) < math.sqrt(
        (best_food.rect.x - man.rect.x) ** 2 + (best_food.rect.y - man.rect.y) ** 2) and foods.sprites()[
        i].rect.x != man.rect.x and foods.sprites()[i].rect.y != man.rect.x:
        best_food = foods.sprites()[i]
m = best_food

# Цикл игры
satiety = 0
ti = 0
running = True
while running:
    ti += 1
    if ti == 400:
        ti = 0
        daynight += 1
        if satiety < 10:
            man.kill()
        if daynight % 2 == 1:
            print("наступила ночь")
            grey = (0, 0, 60)
        else:
            print("наступил день")
            grey = (195, 195, 195)
        satiety -= 10
        for i in range(number_of_food):
            m = food()
            all_sprites.add(m)
            foods.add(m)
        best_food = foods.sprites()[0]
        for i in range(len(foods.sprites())):
            if math.sqrt((foods.sprites()[i].rect.x - man.rect.x) ** 2 + (
                    foods.sprites()[i].rect.y - man.rect.y) ** 2) < math.sqrt(
                (best_food.rect.x - man.rect.x) ** 2 + (best_food.rect.y - man.rect.y) ** 2) and foods.sprites()[
                i].rect.x != man.rect.x and foods.sprites()[i].rect.y != man.rect.x:
                best_food = foods.sprites()[i]
        m = best_food

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    hits3 = pygame.sprite.spritecollide(man, foods, False)
    if hits3:
        satiety += 1

    hits = pygame.sprite.groupcollide(foods, players, True, False)
    if hits and len(foods.sprites()) != 0:
        best_food = foods.sprites()[0]
        for i in range(len(foods.sprites())):
            if math.sqrt((foods.sprites()[i].rect.x - man.rect.x) ** 2 + (
                    foods.sprites()[i].rect.y - man.rect.y) ** 2) < math.sqrt(
                (best_food.rect.x - man.rect.x) ** 2 + (best_food.rect.y - man.rect.y) ** 2) and foods.sprites()[
                i].rect.x != man.rect.x and foods.sprites()[i].rect.y != man.rect.x:
                best_food = foods.sprites()[i]
        m = best_food
    elif hits and len(foods.sprites()) == 0:
        print('сытость = ', satiety + 1)

    screen.fill(grey)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
