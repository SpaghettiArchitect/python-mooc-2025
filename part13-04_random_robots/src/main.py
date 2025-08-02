from random import randint

import pygame

HEIGHT = 480
WIDTH = 640

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))

robot = pygame.image.load(r"src\robot.png")

window.fill((0, 0, 0))

img_width = robot.get_width()
img_height = robot.get_height()

for _ in range(1000):
    x_pos = randint(0, WIDTH - img_width)
    y_pos = randint(0, HEIGHT - img_height)
    window.blit(robot, (x_pos, y_pos))


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
