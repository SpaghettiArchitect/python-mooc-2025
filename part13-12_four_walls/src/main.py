import pygame

WIDTH = 640
HEIGHT = 480

ROBOT_SPEED = 2

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))

robot = pygame.image.load(r"src\robot.png")

x = (WIDTH - robot.get_width()) / 2
y = (HEIGHT - robot.get_height()) / 2

to_right = False
to_left = False
to_up = False
to_down = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_UP:
                to_up = True
            if event.key == pygame.K_DOWN:
                to_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                to_up = False
            if event.key == pygame.K_DOWN:
                to_down = False

        if event.type == pygame.QUIT:
            exit()

    if to_right and x + robot.get_width() <= WIDTH:
        x += ROBOT_SPEED
    if to_left and x >= 0:
        x -= ROBOT_SPEED
    if to_up and y >= 0:
        y -= ROBOT_SPEED
    if to_down and y + robot.get_height() <= HEIGHT:
        y += ROBOT_SPEED

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)
