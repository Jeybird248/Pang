import pygame
############################################
pygame.init()  # starts game instance

# screen size settings
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# title
pygame.display.set_caption("Game Name")

# fps
clock = pygame.time.Clock()
############################################

# 1. Initializing Game Variables (background image, game sprites, position, speed, font, etc)


# game loop
running = True
while running:
    dt = clock.tick(60)  # set FPS

    # 2. Event Handling (user input, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 3. changing sprite positions
    # 4. checking for collision
    # 5. displaying sprites

    pygame.display.update()
pygame.quit()
