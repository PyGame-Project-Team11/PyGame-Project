import pygame, time

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
current_background_index = 1
current_background = backgrounds[current_background_index]
current_background_changed = False

key_mappings = {pygame.K_1: 0, pygame.K_2: 1, pygame.K_3: 2, pygame.K_4: 3}

# icon = pygame.image.load('images/icon.png')
# pygame.display.set_icon(icon)

myfont = pygame.font.Font('fonts/static/PixelifySans-Bold.ttf', 20)

start_button_surf = myfont.render('Start', True, 'white')
start_button = pygame.Rect(200, 200, 120, 60)
start_button.center = (500, 460)

start_transparent_surface = pygame.Surface((WIDTH * 0.8, HEIGHT * 0.8), pygame.SRCALPHA)
start_transparent_surface.fill((200, 200, 200, 200))
greeting = 0  # True

rules_button_surf = myfont.render('Rules', True, 'white')
rules_button = pygame.Rect(200, 200, 100, 60)
rules_button.center = (WIDTH - 100, 50)

rules_transparent_surface = pygame.Surface((650, 220), pygame.SRCALPHA)
rules_transparent_surface.fill((200, 200, 200, 200))
rules_show = 0  # False

ok_button_surf = myfont.render('OK', True, 'white')
ok_button = pygame.Rect(200, 200, 80, 40)
ok_button.center = (840, 280)

option_choose = False
option = False
day1 = True

player_anim_count = 0
is_moving_left = False
is_moving_right = False
last_movement = True


class Player:

    def __init__(self):
        self.health = 70
        self.grades = 0
        self.happiness = 80
        self.finances = 100000
        self.friends = 0
        self.pos_x = 400
        self.pos_y = 420
        self.speed = 15

        self.heart_full = pygame.image.load('images/stats/full_heart.png')
        self.heart_empty = pygame.image.load('images/stats/empty_heart.png')
        self.heart_width = self.heart_full.get_width()
        self.heart_height = self.heart_full.get_height()

        # PLayer walk
        self.walk_left = [
            pygame.image.load('images/player/p_left.png'),
            pygame.image.load('images/player/p_left_move1.png'),
            pygame.image.load('images/player/p_left_move2.png')]
        self.walk_right = [
            pygame.image.load('images/player/p_right.png'),
            pygame.image.load('images/player/p_right_move1.png'),
            pygame.image.load('images/player/p_right_move2.png')]
        self.walk_back = [
            pygame.image.load('images/player/p_back.png'),
            pygame.image.load('images/player/p_back_move1.png'),
            pygame.image.load('images/player/p_back_move2.png')]
        self.walk_forward = [
            pygame.image.load('images/player/player.png'),
            pygame.image.load('images/player/p_move1.png'),
            pygame.image.load('images/player/p_move2.png')]

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

def background_change(n):
    global current_background
    screen.fill("black")
    text_font = pygame.font.Font('fonts/static/PixelifySans-Bold.ttf', 40)
    text = text_font.render("Moving to next location", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (WIDTH//2, HEIGHT//2)
    screen.blit(text, text_rect)
    pygame.display.update()
    time.sleep(0.5)
    current_background = backgrounds[n]
    return n

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rules_button.collidepoint(event.pos):
                rules_show = True
            if ok_button.collidepoint(event.pos):
                rules_show = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                current_background_index = background_change(current_background_index+1)
                current_background_changed = True
            if event.key == pygame.K_LEFT:
                is_moving_left = True
            if event.key == pygame.K_RIGHT:
                is_moving_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                is_moving_left = False
                last_movement = True
            if event.key == pygame.K_RIGHT:
                is_moving_right = False
                last_movement = False
            # to test to change background
            if event.key in key_mappings:
                current_background_index = key_mappings[event.key]
                current_background = backgrounds[current_background_index]
                current_background_changed = True

    if current_background_changed:
        WIDTH = current_background.get_width()
        HEIGHT = current_background.get_height()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        current_background_changed = False

    screen.fill("black")
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
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    greeting = False

        pygame.display.update()
        clock.tick(15)

    player.draw_stats(screen)

    pygame.draw.rect(screen, (100, 100, 100), rules_button)
    screen.blit(rules_button_surf, (rules_button.x + 25, rules_button.y + 17))

    if rules_show:
        screen.blit(rules_transparent_surface, (WIDTH * 0.3, 100))
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

    if is_moving_right and not is_moving_left:
        player.pos_x += player.speed
        player.pos_x = min(950, player.pos_x)
        screen.blit(player.walk_right[player_anim_count], (player.pos_x, player.pos_y))
        player_anim_count = (player_anim_count + 1) % len(player.walk_right)
    elif is_moving_left and not is_moving_right:
        player.pos_x -= player.speed
        player.pos_x = max(0, player.pos_x)
        screen.blit(player.walk_left[player_anim_count], (player.pos_x, player.pos_y))
        player_anim_count = (player_anim_count + 1) % len(player.walk_left)
    elif last_movement:
        screen.blit(player.walk_left[0], (player.pos_x, player.pos_y))
    else:
        screen.blit(player.walk_right[0], (player.pos_x, player.pos_y))

    #Game starts here
    #Day 1 - Sep 4
    if day1:
        text_transparent_surface = pygame.Surface((540, 150), pygame.SRCALPHA)
        text_transparent_surface.fill((230, 230, 230, 200))
        screen.blit(text_transparent_surface, (200, 50))
        text = [
            "Good morning, student, today is your first day!",
            "Unfortunately, you are running late",
            "but you don’t want to miss everything, do you?"]
        for i, t in enumerate(text):
            text_surf = myfont.render(t, True, (0, 0, 0))
            screen.blit(text_surf, (220, i * 30 + 70))
        option_transparent_surface = pygame.Surface((500, 50), pygame.SRCALPHA)
        option_transparent_surface.fill((230, 230, 230, 200))
        option1_surf = myfont.render("NO, I'm ordering a taxi!", True, "black")
        option1 = pygame.Rect(200, 250, 500, 50)
        screen.blit(option_transparent_surface, (200, 250))
        screen.blit(option1_surf, (230, 262))
        option2_surf = myfont.render("Pff, it's nothing serious, I'll take a bus", True, "black")
        option2 = pygame.Rect(200, 320, 500, 50)
        screen.blit(option_transparent_surface, (200, 320))
        screen.blit(option2_surf, (230, 332))
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            mouse_pos = pygame.mouse.get_pos()
            if option1.collidepoint(mouse_pos):
                option_choose = True
                option = True
            elif option2.collidepoint(mouse_pos):
                option_choose = True
                option = False
        if option_choose:
            black_surf = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            for i in range(60):
                black_surf.fill((0,0,0,(i+1)/60*255))
                screen.blit(black_surf, (0, 0))
                pygame.display.update()
                clock.tick(60)
            screen.fill("black")
            text_font = pygame.font.Font('fonts/static/PixelifySans-Bold.ttf', 80)
            if option:
                text = [
                    "You came in time and learned a lot of helpful information!",
                    "Now you are ready to start your life as a student",
                    "",
                    "stats:",
                    "-1230 tenge",
                    "+5 happiness"]
                for i, t in enumerate(text):
                    text_surf = myfont.render(t, False, "white")
                    screen.blit(text_surf, (200, i * 40 + 100))
                player.finances -= 1230
                player.happiness += 5
            else:
                text = [
                    "Unfortunately, you missed a lot of helpful information",
                    "that will be needed in future. Be careful next time!",
                    "",
                    "stats:",
                    "-100 tenge",
                    "-5 happiness"]
                for i, t in enumerate(text):
                    text_surf = myfont.render(t, True, "white")
                    screen.blit(text_surf, (200, i * 40 + 100))
                player.finances -= 100
                player.happiness -= 5
            pygame.display.update()
            time.sleep(1.5)
            current_background = backgrounds[0]
            day1 = False

    pygame.display.update()
    clock.tick(15)
pygame.quit()