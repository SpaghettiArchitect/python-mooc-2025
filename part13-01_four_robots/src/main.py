# The exercises in this part of the course have no automated tests, as the results as visually verified.
# The tests grant points automatically as you submit your solution to the server, no matter what your implementation.
# Only submit your solution when you are ready, and your solution matches the exercise description.
# The exercises may not have automatic tests, but the course staff will still see your solution.
# If your solution clearly does not match the exercise description, you may lose the points granted for the exercises in this part.

# WRITE YOUR SOLUTION HERE:
import pygame

HEIGHT = 480
WIDTH = 640

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))

robot = pygame.image.load(r"src\robot.png")

window.fill((0, 0, 0))
img_width = robot.get_width()
img_height = robot.get_height()
window.blit(robot, (0, 0))
window.blit(robot, (WIDTH - img_width, 0))
window.blit(robot, (0, HEIGHT - img_height))
window.blit(robot, (WIDTH - img_width, HEIGHT - img_height))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
