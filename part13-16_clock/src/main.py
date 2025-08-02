import math
from datetime import datetime

import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480

HOUR_ANGLE = 2 * math.pi / 12
SEC_ANGLE = 2 * math.pi / 60
MIN_ANGLE = 2 * math.pi / 60

# Changes the starting position of the angles, so they start
# at 90 degrees instead of 0 degrees
ANGLE_RECTIFIER = 3 / 2 * math.pi

CENTER = (WIDTH / 2, HEIGHT / 2)

CIRCLE_RADIUS = 200

window = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    time = datetime.now()

    coord_hour = (
        CENTER[0]
        + math.cos(HOUR_ANGLE * (time.hour % 12) + ANGLE_RECTIFIER)
        * (CIRCLE_RADIUS - 50),
        CENTER[1]
        + math.sin(HOUR_ANGLE * (time.hour % 12) + ANGLE_RECTIFIER)
        * (CIRCLE_RADIUS - 50),
    )

    coord_min = (
        CENTER[0]
        + math.cos(MIN_ANGLE * time.minute + ANGLE_RECTIFIER) * (CIRCLE_RADIUS - 25),
        CENTER[1]
        + math.sin(MIN_ANGLE * time.minute + ANGLE_RECTIFIER) * (CIRCLE_RADIUS - 25),
    )

    coord_sec = (
        CENTER[0]
        + math.cos(SEC_ANGLE * time.second + ANGLE_RECTIFIER) * (CIRCLE_RADIUS - 25),
        CENTER[1]
        + math.sin(SEC_ANGLE * time.second + ANGLE_RECTIFIER) * (CIRCLE_RADIUS - 25),
    )

    pygame.display.set_caption(time.strftime("%H:%M:%S"))
    window.fill((0, 0, 0))

    # Draws the reloj figure
    pygame.draw.circle(window, (255, 0, 0), CENTER, CIRCLE_RADIUS, 3)
    pygame.draw.circle(window, (255, 0, 0), CENTER, 10)

    # Hour hand
    pygame.draw.line(window, (0, 0, 255), CENTER, coord_hour, 4)
    # Minute hand
    pygame.draw.line(window, (0, 0, 255), CENTER, coord_min, 2)
    # Second hand
    pygame.draw.line(window, (0, 0, 255), CENTER, coord_sec)

    pygame.display.flip()

    clock.tick(60)
