import pygame

HEIGHT = 480
WIDTH = 640

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))

robot = pygame.image.load(r"src\robot.png")

window.fill((0, 0, 0))

img_width = robot.get_width()
img_height = robot.get_height()

x_pos = img_width
y_pos = img_height

for row in range(1, 11):
    for col in range(1, 11):
        window.blit(robot, (x_pos, y_pos))
        x_pos += img_width - 10
    x_pos = img_width + (img_width / 5 * row)
    y_pos = img_height + (img_height / 4 * row)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
