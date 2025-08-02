import pygame

WIDTH = 640
HEIGHT = 480
SPEED = 3

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))

ball = pygame.image.load(r"src/ball.png")

clock = pygame.time.Clock()

x_pos = 0
y_pos = 0

x_speed = SPEED
y_speed = SPEED

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(ball, (x_pos, y_pos))
    pygame.display.flip()

    x_pos += x_speed
    y_pos += y_speed

    if x_pos + ball.get_width() >= WIDTH or x_pos <= 0:
        x_speed *= -1

    if y_pos + ball.get_height() >= HEIGHT or y_pos <= 0:
        y_speed *= -1

    clock.tick(60)
