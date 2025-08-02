from random import randint

import pygame

WIDTH = 640
HEIGHT = 480

ROBOT_SPEED = 4
ASTEROID_SPEED = 2

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroids")

game_font = pygame.font.SysFont("Arial", 24)

robot_img = pygame.image.load(r"src\robot.png").convert()
robot_rect = robot_img.get_rect()

robot_x = WIDTH / 2 - robot_img.get_width() / 2
robot_y = HEIGHT - robot_img.get_height()

asteroid_img = pygame.image.load(r"src\rock.png").convert()

clock = pygame.time.Clock()

controls = {pygame.K_LEFT: False, pygame.K_RIGHT: False}


def get_random_x():
    return randint(0, WIDTH - asteroid_img.get_width())


def get_random_y():
    return -randint(asteroid_img.get_height(), 8000) - asteroid_img.get_height()


asteroids = []

for _ in range(10):
    new_asteroid = pygame.Rect(
        get_random_x(),
        get_random_y(),
        asteroid_img.get_width(),
        asteroid_img.get_height(),
    )
    asteroids.append(new_asteroid)

loser_zone = pygame.Rect(0, HEIGHT, WIDTH, 300)

points = 0

game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key in controls:
                controls[event.key] = True

        if event.type == pygame.KEYUP:
            if event.key in controls:
                controls[event.key] = False

    if game_over:
        screen.fill((0, 0, 0))
        game_font.set_bold(True)
        text = game_font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(
            text, ((WIDTH - text.get_width()) / 2, (HEIGHT - text.get_height()) / 2)
        )
        pygame.display.flip()
        continue

    if controls[pygame.K_LEFT] and robot_x >= 0:
        robot_x -= ROBOT_SPEED
    if controls[pygame.K_RIGHT] and robot_x + robot_img.get_width() <= WIDTH:
        robot_x += ROBOT_SPEED

    screen.fill((0, 0, 0))

    screen.blit(robot_img, (robot_x, robot_y))
    robot_rect.topleft = (robot_x, robot_y)

    for asteroid in asteroids:
        if loser_zone.colliderect(asteroid):
            game_over = True

        if robot_rect.colliderect(asteroid):
            points += 1
            asteroid.left = get_random_x()
            asteroid.top = get_random_y()
        screen.blit(asteroid_img, (asteroid.left, asteroid.top))
        asteroid.top += ASTEROID_SPEED

    text = game_font.render(f"Points: {points}", True, (255, 0, 0))
    screen.blit(text, (WIDTH - text.get_width() - 20, 20))

    pygame.display.flip()

    clock.tick(60)
