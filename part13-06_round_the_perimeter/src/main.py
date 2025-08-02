import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480
SPEED = 1

window = pygame.display.set_mode((WIDTH, HEIGHT))

robot = pygame.image.load(r"src/robot.png")

x_pos = 0
y_pos = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x_pos, y_pos))
    pygame.display.flip()

    if x_pos + robot.get_width() >= WIDTH:
        y_speed = SPEED
        x_speed = 0

    if y_pos + robot.get_height() >= HEIGHT:
        x_speed = -SPEED
        y_speed = 0

    if x_pos <= 0 and y_pos > 0:
        x_speed = 0
        y_speed = -SPEED

    if y_pos <= 0 and x_pos <= 0:
        x_speed = SPEED
        y_speed = 0

    x_pos += x_speed
    y_pos += y_speed

    clock.tick(60)
