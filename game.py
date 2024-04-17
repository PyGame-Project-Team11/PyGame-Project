import pygame

clock = pygame.time.Clock()
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("proj n11")

transparent_surface = pygame.Surface((WIDTH*0.8, HEIGHT*0.8), pygame.SRCALPHA)
transparent_surface.fill((200, 200, 200, 200))
greeting = True

# icon = pygame.image.load('images/icon.png')
# pygame.display.set_icon(icon)

myfont = pygame.font.SysFont('comicsansms', 20)

button_surf = myfont.render('Start', True, 'white')
button = pygame.Rect(200, 200, 110, 60)
button.center = (WIDTH//2, HEIGHT//2 + 100)

background = pygame.image.load('images/background.png')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

walk_left = [
    pygame.image.load('images/player_left/player_left1.png'),
    pygame.image.load('images/player_left/player_left2.png'),
    pygame.image.load('images/player_left/player_left3.png')
]
walk_right = [
    pygame.image.load('images/player_right/player_right1.png'),
    pygame.image.load('images/player_right/player_right2.png'),
    pygame.image.load('images/player_right/player_right3.png')
]
player_anim_count = 0
is_moving_left = False
is_moving_right = False
last_movement = True

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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                t = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                t = False

    screen.blit(background, (0, 0))

    if not greeting:
        player.draw_stats(screen)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.pos_x > 0:
            player.pos_x -= player.speed
            is_moving_left = True
            last_movement = True
        elif keys[pygame.K_RIGHT] and player.pos_x < 760:
            player.pos_x += player.speed
            is_moving_right = True
            last_movement = False
        else:
            is_moving_left = False
            is_moving_right = False

        if is_moving_right:
            screen.blit(walk_right[player_anim_count], (player.pos_x, player.pos_y))
            player_anim_count = (player_anim_count + 1) % len(walk_right)
        elif is_moving_left:
            screen.blit(walk_left[player_anim_count], (player.pos_x, player.pos_y))
            player_anim_count = (player_anim_count + 1) % len(walk_left)
        elif last_movement:
            screen.blit(walk_left[0], (player.pos_x, player.pos_y))
        else:
            screen.blit(walk_right[0], (player.pos_x, player.pos_y))

    else:
        screen.blit(transparent_surface, (WIDTH*0.1, HEIGHT*0.1))
        greeting_text = [
            "Hi!",
            "To play this game imagine that you are a student",
            "of KBTU from another city.",
            "Try to survive until the end of semester.",
            "",
            "Remember, every action has its own consequences."
        ]
        for i, text in enumerate(greeting_text):
            text_surface = myfont.render(text, True, (0, 0, 0))
            screen.blit(text_surface, (100, i * 30 + 100))

        a, b = pygame.mouse.get_pos()
        if button.x <= a <= button.x + 110 and button.y <= b <= button.y + 60:
            pygame.draw.rect(screen, (180, 180, 180), button)
        else:
            pygame.draw.rect(screen, (110, 110, 110), button)
        screen.blit(button_surf, (button.x + 26, button.y + 14))

    pygame.display.update()
    clock.tick(15)
pygame.quit()