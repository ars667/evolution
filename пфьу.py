import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Steam Dry")

bg = pygame.image.load("bg.png")
bgu = bg.get_rect()
win.blit(bg, bgu)

x = 50
y = 425
width = 40
height = 60
speed = 10

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 500 - width - 5:
        x += speed
    if keys[pygame.K_UP] and y > 5:
        y -= speed
    if keys[pygame.K_DOWN] and y < 500 - height - 15:
        y += speed

    pygame.draw.rect(win, (	100, 42, 42), (x, y, width, height))
    #pygame.sprite()
    pygame.display.update()

pygame.quit()