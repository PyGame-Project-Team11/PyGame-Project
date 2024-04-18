import pygame

clock = pygame.time.Clock()
pygame.init()
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("proj n11")

background_list = [
    {'image': 'images/background.png'},
    {'image': 'images/dorm.png'},
    {'image': 'images/hall.png'},
    {'image': 'images/street.png'}]
backgrounds = [pygame.transform.scale(pygame.image.load(image['image']), (WIDTH, HEIGHT)) for image in background_list]
current_background_index = 0
current_background = backgrounds[current_background_index]
current_background_changed = False

key_mappings = {pygame.K_1: 0, pygame.K_2: 1, pygame.K_3: 2, pygame.K_4: 3}

# icon = pygame.image.load('images/icon.png')
# pygame.display.set_icon(icon)

myfont = pygame.font.Font('fonts/static/PixelifySans-Bold.ttf', 20)

start_button_surf = myfont.render('Start', True, 'white')
start_button = pygame.Rect(200, 200, 120, 60)
start_button.center = (500, 460)

start_transparent_surface = pygame.Surface((WIDTH*0.8, HEIGHT*0.8), pygame.SRCALPHA)
start_transparent_surface.fill((200, 200, 200, 200))
greeting = 1 #True

rules_button_surf = myfont.render('Rules', True, 'white')
rules_button = pygame.Rect(200, 200, 100, 60)
rules_button.center = (WIDTH - 100, 50)

rules_transparent_surface = pygame.Surface((620, 220), pygame.SRCALPHA)
rules_transparent_surface.fill((200, 200, 200, 200))
rules_show = 0 #False

ok_button_surf = myfont.render('OK', True, 'white')
ok_button = pygame.Rect(200, 200, 80, 40)
ok_button.center = (840, 280)

walk_left = [
    pygame.image.load('images/player_left/player_left1.png'),
    pygame.image.load('images/player_left/player_left2.png'),
    pygame.image.load('images/player_left/player_left3.png')]
walk_right = [
    pygame.image.load('images/player_right/player_right1.png'),
    pygame.image.load('images/player_right/player_right2.png'),
    pygame.image.load('images/player_right/player_right3.png')]
player_anim_count = 0
is_moving_left = False
is_moving_right = False
last_movement = True

class Player:

    def __init__(self):
        self.health = 70
        self.grades = 0
        self.happiness = 80
        self.finances = 100.000
        self.friends = 0
        self.pos_x = 400
        self.pos_y = 420
        self.speed = 10

        self.heart_full = pygame.image.load('images/stats/full_heart.png')
        self.heart_empty = pygame.image.load('images/stats/empty_heart.png')
        self.heart_width = self.heart_full.get_width()
        self.heart_height = self.heart_full.get_height()

        self.friend_icon = pygame.image.load(
            'images/stats/friends_icon.png')  # Load friend icon
        self.friend_icon_width = self.friend_icon.get_width()
        self.friend_icon_height = self.friend_icon.get_height()

    def draw_stats(self, screen):
        # stats = [
        #     f"Grades: {self.grades}", f"Happiness: {self.happiness}",
        #     f"Finances: {self.finances}k tg"
        # ]
        # for i, stat in enumerate(stats):
        #     text_surface = myfont.render(stat, True, (255, 255, 255))
        #     screen.blit(text_surface, (20, i * 25 + 10))

        hearts_to_draw = self.health // 10
        last_pos = 0
        for i in range(hearts_to_draw):
            screen.blit(self.heart_full, (20 + i * (self.heart_width + 5), 10))
            last_pos = 20 + i * (self.heart_width + 5)
        for i in range(10 - hearts_to_draw):
            screen.blit(self.heart_empty,
                        (last_pos + i * (self.heart_width + 5), 10))

        screen.blit(self.friend_icon, (45, 40))
        friends_text = myfont.render(f"{self.friends}", True, (36, 32, 46))
        screen.blit(friends_text, (self.friend_icon_width, 40))

player = Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                greeting = False
            if rules_button.collidepoint(event.pos):
                rules_show = True
            if ok_button.collidepoint(event.pos):
                rules_show = False
        elif event.type == pygame.KEYDOWN:
            #to test to change background
            if event.key in key_mappings:
                current_background_index = key_mappings[event.key]
                current_background = backgrounds[current_background_index]
                current_background_changed = True

    if current_background_changed:
        WIDTH = current_background.get_width()
        HEIGHT = current_background.get_height()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        current_background_changed = False
    screen.blit(current_background, (0, 0))

    while greeting:
        screen.blit(backgrounds[0], (0, 0))
        screen.blit(start_transparent_surface, (WIDTH * 0.1, HEIGHT * 0.1))
        greeting_text = [
            "Hi!",
            "To play this game imagine that you are a student",
            "of KBTU from another city.",
            "Try to survive until the end of semester.",
            "",
            "Remember, every action has its own consequences."]
        for i, text in enumerate(greeting_text):
            text_surface = myfont.render(text, True, (0, 0, 0))
            screen.blit(text_surface, (WIDTH * 0.15, i * 30 + 100))

        pygame.draw.rect(screen, (100, 100, 100), start_button)
        screen.blit(start_button_surf, (start_button.x + 33, start_button.y + 14))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    greeting = False

        pygame.display.update()
        clock.tick(15)

    player.draw_stats(screen)

    pygame.draw.rect(screen, (100, 100, 100), rules_button)
    screen.blit(rules_button_surf, (rules_button.x + 25, rules_button.y + 17))

    if rules_show:
        screen.blit(rules_transparent_surface, (WIDTH*0.3, 100))
        rules_text = [
            "1. You must survive until 25 December 2023 ",
            "2. Your health status must not go below 30",
            "3. Your grades must not go below 30",
            "4. Every 4 weeks you will automatically get additional finances",
            "5. Live your best student life!"]
        for i, text in enumerate(rules_text):
            text_surface = myfont.render(text, True, (0, 0, 0))
            screen.blit(text_surface, (330, i * 30 + 120))

        pygame.draw.rect(screen, (100, 100, 100), ok_button)
        screen.blit(ok_button_surf, (ok_button.x + 24, ok_button.y + 8))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.pos_x > 0:
        player.pos_x -= player.speed
        is_moving_left = True
        last_movement = True
    elif keys[pygame.K_RIGHT] and player.pos_x < WIDTH - 40:
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

    pygame.display.update()
    clock.tick(15)
pygame.quit()