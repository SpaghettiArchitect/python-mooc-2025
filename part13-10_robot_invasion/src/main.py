from random import choice, randint

import pygame

WIDTH = 640
HEIGHT = 480

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))

robot = pygame.image.load(r"src/robot.png").convert()

clock = pygame.time.Clock()

current_tick = 0

robots_coords = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if current_tick == randint(0, 60) and len(robots_coords) <= 20:
        x_pos = randint(0, WIDTH - robot.get_width())
        y_pos = -robot.get_height()
        robots_coords.append({"x": x_pos, "y": y_pos, "x_speed": 0, "y_speed": 1})

    window.fill((0, 0, 0))

    for coord in robots_coords:
        window.blit(robot, (coord["x"], coord["y"]))

        coord["x"] += coord["x_speed"]
        coord["y"] += coord["y_speed"]

        if (
            coord["y"] + robot.get_height() >= HEIGHT
            and coord["x_speed"] == 0
            and coord["y_speed"] == 1
        ):
            coord["x_speed"] = choice([1, -1])
            coord["y_speed"] = 0

        if coord["x"] + robot.get_width() < 0 or coord["x"] - robot.get_width() > WIDTH:
            robots_coords.remove(coord)

    pygame.display.flip()

    current_tick = clock.tick(60)
