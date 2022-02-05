import pygame

pygame.init()  # starts game instance

# screen size settings
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# title
pygame.display.set_caption("Pang")

# fps
clock = pygame.time.Clock()

# load background iamge
background = pygame.image.load("C:\\Users\\tommy\\PycharmProjects\\Pang\\pygame_basic\\background.png")

# load character sprite
character = pygame.image.load("C:\\Users\\tommy\\PycharmProjects\\Pang\\pygame_basic\\character.png")
character_size = character.get_rect().size  # size of image rectangle (hitbox)
character_width = character_size[0]  # size is stored as [width][height]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height

# move direction
to_x = 0
to_y = 0

# char speed
character_speed = 0.6

# enemy
enemy = pygame.image.load("C:\\Users\\tommy\\PycharmProjects\\Pang\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size  # size of image rectangle (hitbox)
enemy_width = enemy_size[0]  # size is stored as [width][height]
enemy_height = enemy_size[1]
enemy_x_pos = screen_width / 2 - enemy_width / 2
enemy_y_pos = screen_height / 2 - enemy_height / 2

# create new font
game_font = pygame.font.Font(None, 40)  # default font and size 40

# print time
total_time = 10
start_ticks = pygame.time.get_ticks()  # get the tick at the beginning of program run

# game loop
running = True
while running:
    dt = clock.tick(60)  # set FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    # move char
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # block boundaries
    if character_x_pos < 0:
        character_x_pos = 0
    if character_y_pos < 0:
        character_y_pos = 0
    if character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    if character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # hit box setup
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # collision
    if character_rect.colliderect(enemy_rect):
        print("collide")
        running = False

    # show image on screen at 0, 0
    screen.blit(background, (0, 0))

    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    # print the time elapsed
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000  # converting milliseconds to seconds
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))  # display the time remaining
    screen.blit(timer, (10,10))

    if total_time - elapsed_time <= 0:
        running = False

    # thing to display, antialiasing, color
    pygame.display.update()


pygame.time.delay(2000) # wait before quitting

pygame.quit()
