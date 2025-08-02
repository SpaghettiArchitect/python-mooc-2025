import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480
SPEED = 1

window = pygame.display.set_mode((640, 480))

robot1 = pygame.image.load(r"src/robot.png")
robot2 = robot1.copy()

robot1_x = 0
robot1_speed = SPEED

robot2_x = 0
robot2_speed = SPEED * 2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot1, (robot1_x, 50))
    window.blit(robot2, (robot2_x, 50 + robot1.get_height() + 20))
    pygame.display.flip()

    robot1_x += robot1_speed
    robot2_x += robot2_speed

    if robot1_x + robot1.get_width() >= WIDTH or robot1_x <= 0:
        robot1_speed *= -1

    if robot2_x + robot2.get_width() >= WIDTH or robot2_x <= 0:
        robot2_speed *= -1

    clock.tick(60)
