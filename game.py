import pygame, time

clock = pygame.time.Clock()
pygame.init()
SIZE = WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("proj n11")
# icon = pygame.image.load('images/icon.png')
# pygame.display.set_icon(icon)

myfont = pygame.font.SysFont('comicsansms', 20)
text_surface = myfont.render('some text', True, 'Red')

background = pygame.image.load('images/background.png')
background = pygame.transform.scale(background, SIZE)

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
# Start game
start = True 
start_font1 = pygame.font.SysFont('arial', 35)
start_hi = start_font1.render('Hi!', True, (255, 255, 255))
start_hi_rect = start_hi.get_rect()
start_hi_rect.center = (WIDTH//2, HEIGHT//2)

start_font2 = pygame.font.SysFont('arial', 20)
start_text1 = start_font2.render('To play this game imagine that you are a student of KBTU from another city.', True, (255, 255, 255))
start_text2 = start_font2.render('Try to survive until the end of semester.', True, (255, 255, 255))
start_text3 = start_font2.render('Remember, every action has its own consequences.', True, (255, 255, 255))

start_text1_rect = start_text1.get_rect()
start_text1_rect.center = (WIDTH//2, HEIGHT//2-20)
start_text2_rect = start_text2.get_rect()
start_text2_rect.center = (WIDTH//2, HEIGHT//2)
start_text3_rect = start_text3.get_rect()
start_text3_rect.center = (WIDTH//2, HEIGHT//2+20)

while running:
    
    while start:
        screen.fill((0, 0, 0))
        screen.blit(start_hi, start_hi_rect)
        pygame.display.update()
        time.sleep(1)
        screen.fill((0, 0, 0))
        screen.blit(start_text1, start_text1_rect)
        screen.blit(start_text2, start_text2_rect)
        screen.blit(start_text3, start_text3_rect)
        
        pygame.display.update()
        time.sleep(2)
        start = False
    
    screen.blit(background, (0, 0))
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
        screen.blit(walk_right[player_anim_count],
                    (player.pos_x, player.pos_y))
        player_anim_count = (player_anim_count + 1) % len(walk_right)
    elif is_moving_left:
        screen.blit(walk_left[player_anim_count],
                    (player.pos_x, player.pos_y))
        player_anim_count = (player_anim_count + 1) % len(walk_left)
    elif last_movement:
        screen.blit(walk_left[0], (player.pos_x, player.pos_y))
    else:
        screen.blit(walk_right[0], (player.pos_x, player.pos_y))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_a:

    clock.tick(15)