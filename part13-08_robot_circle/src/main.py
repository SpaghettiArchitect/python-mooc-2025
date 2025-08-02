import math

import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480
IMG_SEPARATION = 2 * math.pi / 10
CIRCLE_RADIUS = 130

window = pygame.display.set_mode((WIDTH, HEIGHT))

robot = pygame.image.load(r"src/robot.png").convert()

angle = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    for i in range(10):
        x = (
            WIDTH / 2
            + math.cos(angle + IMG_SEPARATION * i) * CIRCLE_RADIUS
            - robot.get_width() / 2
        )
        y = (
            HEIGHT / 2
            + math.sin(angle + IMG_SEPARATION * i) * CIRCLE_RADIUS
            - robot.get_height() / 2
        )
        window.blit(robot, (x, y))

    pygame.display.flip()

    angle += 0.01
    clock.tick(60)
