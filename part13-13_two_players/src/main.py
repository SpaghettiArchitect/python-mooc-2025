import pygame

WIDTH = 640
HEIGHT = 480
ROBOT_SPEED = 2

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))

robot_img = pygame.image.load(r"src\robot.png")

robot1 = {
    "x": (WIDTH - robot_img.get_width()) / 2,
    "y": (HEIGHT - robot_img.get_height()) / 2,
    "up": False,
    "down": False,
    "left": False,
    "right": False,
}

robot2 = {
    "x": (WIDTH + robot_img.get_width()) / 2,
    "y": (HEIGHT - robot_img.get_height()) / 2,
    "up": False,
    "down": False,
    "left": False,
    "right": False,
}

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # Cases for the robot with the up, down, left and right keys
            if event.key == pygame.K_LEFT:
                robot1["left"] = True
            if event.key == pygame.K_RIGHT:
                robot1["right"] = True
            if event.key == pygame.K_UP:
                robot1["up"] = True
            if event.key == pygame.K_DOWN:
                robot1["down"] = True
            # Cases fot the robot with the w, s, a and d keys
            if event.key == pygame.K_a:
                robot2["left"] = True
            if event.key == pygame.K_d:
                robot2["right"] = True
            if event.key == pygame.K_w:
                robot2["up"] = True
            if event.key == pygame.K_s:
                robot2["down"] = True

        if event.type == pygame.KEYUP:
            # Cases for the robot with the up, down, left and right keys
            if event.key == pygame.K_LEFT:
                robot1["left"] = False
            if event.key == pygame.K_RIGHT:
                robot1["right"] = False
            if event.key == pygame.K_UP:
                robot1["up"] = False
            if event.key == pygame.K_DOWN:
                robot1["down"] = False
            # Cases for the robot with the w, s, a and d keys
            if event.key == pygame.K_a:
                robot2["left"] = False
            if event.key == pygame.K_d:
                robot2["right"] = False
            if event.key == pygame.K_w:
                robot2["up"] = False
            if event.key == pygame.K_s:
                robot2["down"] = False

        if event.type == pygame.QUIT:
            exit()

    # Movements for robot1
    if robot1["up"]:
        robot1["y"] -= ROBOT_SPEED
    if robot1["down"]:
        robot1["y"] += ROBOT_SPEED
    if robot1["left"]:
        robot1["x"] -= ROBOT_SPEED
    if robot1["right"]:
        robot1["x"] += ROBOT_SPEED

    # Movements for robot2
    if robot2["up"]:
        robot2["y"] -= ROBOT_SPEED
    if robot2["down"]:
        robot2["y"] += ROBOT_SPEED
    if robot2["left"]:
        robot2["x"] -= ROBOT_SPEED
    if robot2["right"]:
        robot2["x"] += ROBOT_SPEED

    window.fill((0, 0, 0))
    window.blit(robot_img, (robot2["x"], robot2["y"]))
    window.blit(robot_img, (robot1["x"], robot1["y"]))
    pygame.display.flip()

    clock.tick(60)
