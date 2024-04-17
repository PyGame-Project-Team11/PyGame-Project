import pygame

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("proj n11")
# icon = pygame.image.load('images/icon.png')
# pygame.display.set_icon(icon)

myfont = pygame.font.SysFont('comicsansms', 20)
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
is_moving = False


class Player:

    def __init__(self):
        self.health = 70
        self.grades = 100
        self.happiness = 80
        self.finances = 100000
        self.sleepiness = 10
        self.stress = 10
        self.friends = 0
        self.pos_x = 300
        self.pos_y = 420
        self.speed = 10

    def draw_stats(self, screen):
        stats = [
            f"Health: {self.health}", f"Grades: {self.grades}",
            f"Happiness: {self.happiness}", f"Finances:{self.finances} ₸",
            f"Sleepiness: {self.sleepiness}", f"Stress: {self.stress}",
            f"Friends: {self.friends}"
        ]
        for i, stat in enumerate(stats):
            text_surface = myfont.render(stat, True, (255, 255, 255))
            screen.blit(text_surface, (10, i * 20))


player = Player()

running = True
while running:
    screen.blit(background, (0, 0))
    player.draw_stats(screen)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.pos_x > 0:
        player.pos_x -= player.speed
        is_moving = True
    elif keys[pygame.K_RIGHT] and player.pos_x < 760:
        player.pos_x += player.speed
        is_moving = True
    else:
        is_moving = False

    if is_moving:
        screen.blit(walk_right[player_anim_count],
                    (player.pos_x, player.pos_y))
        player_anim_count = (player_anim_count + 1) % len(walk_right)
    else:
        screen.blit(walk_right[0], (player.pos_x, player.pos_y))

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
