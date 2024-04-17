import pygame

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("proj n11")
# icon = pygame.image.load('images/icon.png')
# pygame.display.set_icon(icon)

myfont = pygame.font.SysFont('comicsansms', 40)
text_surface = myfont.render('some text', True, 'Red')

background = pygame.image.load('images/background.png')
background = pygame.transform.scale(background, (800, 600))

# player = pygame.image.load('images/player.png')
# walk_left = [
#     pygame.image.load('images/player_left/player_left1.png'),
#     pygame.image.load('images/player_left/player_left2.png'),
#     pygame.image.load('images/player_left/player_left3.png')
# ]
walk_right = [
    pygame.image.load('images/player_right/player_right1.png'),
    pygame.image.load('images/player_right/player_right2.png'),
    pygame.image.load('images/player_right/player_right3.png')
]
player_anim_count = 0

running = True
while running:
    screen.blit(background, (0, 0))
    screen.blit(walk_right[player_anim_count], (300, 420))

    if player_anim_count == 2:
        player_anim_count = 0
    else:
        player_anim_count += 1
    # screen.blit(text_surface, (100, 50))
    # screen.blit(player, (200, 100))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                screen.fill((70, 44, 133))

    clock.tick(15)
