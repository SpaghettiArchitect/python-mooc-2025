import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load(r"src\robot.png")

x_pos = 0
y_pos = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            x_pos = event.pos[0] - robot.get_width() / 2
            y_pos = event.pos[1] - robot.get_height() / 2

        if event.type == pygame.QUIT:
            exit(0)

    window.fill((0, 0, 0))
    window.blit(robot, (x_pos, y_pos))
    pygame.display.flip()

    clock.tick(60)
