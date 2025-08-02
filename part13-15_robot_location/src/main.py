from random import randint

import pygame

WIDTH = 640
HEIGHT = 480

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))

robot = pygame.image.load(r"src\robot.png")

x_pos = randint(0, WIDTH - robot.get_width())
y_pos = randint(0, HEIGHT - robot.get_height())


def get_boundaries(x_pos: int, y_pos: int, img_width: int, img_height: int):
    return {
        "left": x_pos,
        "right": x_pos + img_width,
        "upper": y_pos,
        "lower": y_pos + img_height,
    }


while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            bounds = get_boundaries(x_pos, y_pos, robot.get_width(), robot.get_height())

            if (
                bounds["left"] <= mouse_x <= bounds["right"]
                and bounds["upper"] <= mouse_y <= bounds["lower"]
            ):
                x_pos = randint(0, WIDTH - robot.get_width())
                y_pos = randint(0, HEIGHT - robot.get_height())

        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x_pos, y_pos))
    pygame.display.flip()
