import pygame, time

clock = pygame.time.Clock()
pygame.init()
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("proj n11")

background_images = [
    'images/background.png', 'images/dorm.png', 'images/hall.png',
    'images/street.png', 'images/kbtu_front.png'
]
backgrounds = [
    pygame.transform.scale(pygame.image.load(image), (WIDTH, HEIGHT))
    for image in background_images
]

current_background_index = 1  # 1
current_background = backgrounds[current_background_index]
current_background_changed = False

key_mappings = {
    pygame.K_1: 0,
    pygame.K_2: 1,
    pygame.K_3: 2,
    pygame.K_4: 3,
    pygame.K_5: 4
}

# icon = pygame.image.load('images/icon.png')
# pygame.display.set_icon(icon)

myfont = pygame.font.Font('fonts/static/PixelifySans-Bold.ttf', 20)
myfont2 = pygame.font.Font('fonts/static/PixelifySans-Bold.ttf', 30)

start_button_surf = myfont.render('Start', True, 'white')
start_button = pygame.Rect(200, 200, 120, 60)
start_button.center = (500, 460)

start_transparent_surface = pygame.Surface((WIDTH * 0.8, HEIGHT * 0.8),
                                           pygame.SRCALPHA)
start_transparent_surface.fill((200, 200, 200, 200))
greeting = 1  # True

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
day2, day3, day4, day5 = False, False, False, False

club_join = False

player_anim_count = 0
is_moving_left = False
is_moving_right = False
last_movement = False


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
            pygame.image.load('images/player/p_left_move2.png')
        ]
        self.walk_right = [
            pygame.image.load('images/player/p_right.png'),
            pygame.image.load('images/player/p_right_move1.png'),
            pygame.image.load('images/player/p_right_move2.png')
        ]
        self.walk_back = [
            pygame.image.load('images/player/p_back.png'),
            pygame.image.load('images/player/p_back_move1.png'),
            pygame.image.load('images/player/p_back_move2.png')
        ]
        self.walk_forward = [
            pygame.image.load('images/player/player.png'),
            pygame.image.load('images/player/p_move1.png'),
            pygame.image.load('images/player/p_move2.png')
        ]

        self.friend_icon = pygame.image.load(
            'images/stats/friends_icon.png')  # Load friend icon
        self.friend_icon_width = self.friend_icon.get_width()
        self.friend_icon_height = self.friend_icon.get_height()

        self.coin = pygame.image.load('images/stats/coin.png')
        self.coin_width = self.coin.get_width()

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

        screen.blit(self.coin, (len(str(self.finances)) * 15 + 10, 65))
        coin_text = myfont.render(f"{self.finances}", True, (36, 32, 46))
        screen.blit(coin_text, (self.coin_width, 65))


player = Player()


def background_change(n):
    global current_background
    screen.fill("black")
    text = myfont2.render("Moving to next location", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (WIDTH // 2, HEIGHT // 2)
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
                current_background_index = background_change(
                    current_background_index + 1)
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
            "Hi!", "To play this game imagine that you are a student",
            "of KBTU from another city.",
            "Try to survive until the end of semester.", "",
            "Remember, every action has its own consequences."
        ]
        for i, text in enumerate(greeting_text):
            text_surface = myfont.render(text, True, (0, 0, 0))
            screen.blit(text_surface, (WIDTH * 0.15, i * 30 + 100))

        pygame.draw.rect(screen, (100, 100, 100), start_button)
        screen.blit(start_button_surf,
                    (start_button.x + 33, start_button.y + 14))

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
            "5. Live your best student life!"
        ]
        for i, text in enumerate(rules_text):
            text_surface = myfont.render(text, True, (0, 0, 0))
            screen.blit(text_surface, (330, i * 30 + 120))

        pygame.draw.rect(screen, (100, 100, 100), ok_button)
        screen.blit(ok_button_surf, (ok_button.x + 24, ok_button.y + 8))

    if is_moving_right and not is_moving_left:
        player.pos_x += player.speed
        player.pos_x = min(950, player.pos_x)
        screen.blit(player.walk_right[player_anim_count],
                    (player.pos_x, player.pos_y))
        player_anim_count = (player_anim_count + 1) % len(player.walk_right)
    elif is_moving_left and not is_moving_right:
        player.pos_x -= player.speed
        player.pos_x = max(0, player.pos_x)
        screen.blit(player.walk_left[player_anim_count],
                    (player.pos_x, player.pos_y))
        player_anim_count = (player_anim_count + 1) % len(player.walk_left)
    elif last_movement:
        screen.blit(player.walk_left[0], (player.pos_x, player.pos_y))
    else:
        screen.blit(player.walk_right[0], (player.pos_x, player.pos_y))

    # Game starts here
    # Day 1 - Sep 4
    if day1:
        screen.blit(myfont2.render("September 4", True, "black"), (400, 10))
        text_transparent_surface = pygame.Surface((540, 150), pygame.SRCALPHA)
        text_transparent_surface.fill((230, 230, 230, 200))
        screen.blit(text_transparent_surface, (200, 50))
        text = [
            "Good morning, student, today is your first day!",
            "Unfortunately, you are running late",
            "but you don’t want to miss everything, do you?"
        ]
        for i, t in enumerate(text):
            text_surf = myfont.render(t, True, (0, 0, 0))
            screen.blit(text_surf, (220, i * 30 + 70))
        option_transparent_surface = pygame.Surface((500, 50), pygame.SRCALPHA)
        option_transparent_surface.fill((230, 230, 230, 200))
        option1_surf = myfont.render("NO, I'm ordering a taxi!", True, "black")
        option1 = pygame.Rect(200, 250, 500, 50)
        screen.blit(option_transparent_surface, (200, 250))
        screen.blit(option1_surf, (230, 262))
        option2_surf = myfont.render(
            "Pff, it's nothing serious, I'll take a bus", True, "black")
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
                black_surf.fill((0, 0, 0, (i + 1) / 60 * 255))
                screen.blit(black_surf, (0, 0))
                pygame.display.update()
                clock.tick(120)  # 60
            screen.fill("black")
            # text_font = pygame.font.Font('fonts/static/PixelifySans-Bold.ttf', 80)
            if option:
                text = [
                    "You came in time and learned a lot of helpful information!",
                    "Now you are ready to start your life as a student", "",
                    "stats:", "-1230 tenge", "+5 happiness"
                ]
                for i, t in enumerate(text):
                    text_surf = myfont.render(t, False, "white")
                    screen.blit(text_surf, (200, i * 40 + 100))
                player.finances -= 1230
                player.happiness += 5
            else:
                text = [
                    "Unfortunately, you missed a lot of helpful information",
                    "that will be needed in future. Be careful next time!", "",
                    "stats:", "-100 tenge", "-5 happiness"
                ]
                for i, t in enumerate(text):
                    text_surf = myfont.render(t, True, "white")
                    screen.blit(text_surf, (200, i * 40 + 100))
                player.finances -= 100
                player.happiness -= 5
            pygame.display.update()
            time.sleep(1.5)  # 1.5
            current_background = backgrounds[4]
            player.pos_x = 100
            day2 = True
            option_choose = False
            option = False
            day1 = False

    # Day 2 - Sep 7
    elif day2:
        screen.blit(myfont2.render("September 7", True, "black"), (400, 10))
        npc1 = pygame.image.load('images/characters/f2_right.png')
        npc1 = pygame.transform.scale(npc1, (134 * 0.6, 164))
        npc2 = pygame.image.load('images/characters/f1_left.png')
        npc2 = pygame.transform.scale(npc2, (134 * 0.6, 164))
        screen.blit(npc1, (700, player.pos_y))
        screen.blit(npc2, (840, player.pos_y))
        if not 700 - player.pos_x - 50 < 80:
            text_transparent_surface = pygame.Surface((540, 150),
                                                      pygame.SRCALPHA)
            text_transparent_surface.fill((230, 230, 230, 200))
            screen.blit(text_transparent_surface, (200, 50))
            text = [
                "time to get some friends?",
                "try approaching them by pressing ->"
            ]
            for i, t in enumerate(text):
                text_surf = myfont.render(t, True, (0, 0, 0))
                screen.blit(text_surf, (220, i * 30 + 70))
            pygame.display.update()

        else:
            text_transparent_surface = pygame.Surface((540, 150),
                                                      pygame.SRCALPHA)
            text_transparent_surface.fill((230, 230, 230, 200))
            screen.blit(text_transparent_surface, (200, 50))
            text = ["Do you want to try to talk with them?"]
            for i, t in enumerate(text):
                text_surf = myfont.render(t, True, (0, 0, 0))
                screen.blit(text_surf, (220, i * 30 + 70))
            option_transparent_surface = pygame.Surface((500, 50),
                                                        pygame.SRCALPHA)
            option_transparent_surface.fill((230, 230, 230, 200))
            option1_surf = myfont.render("-Yeah, let's do it", True, "black")
            option1 = pygame.Rect(200, 250, 500, 50)
            screen.blit(option_transparent_surface, (200, 250))
            screen.blit(option1_surf, (230, 262))
            option2_surf = myfont.render("Nah, I’m scared", True, "black")
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
                screen.fill("black")
                # text_font = pygame.font.Font('fonts/static/PixelifySans-Bold.ttf', 80)
                if option:
                    text = [
                        "Nice choice!", "", "stats:", "+2 friends",
                        "+5 happiness"
                    ]
                    for i, t in enumerate(text):
                        text_surf = myfont.render(t, False, "white")
                        screen.blit(text_surf, (200, i * 40 + 100))
                    player.friends += 2
                    player.happiness += 5
                else:
                    text = ["Maybe next time."]
                    for i, t in enumerate(text):
                        text_surf = myfont.render(t, True, "white")
                        screen.blit(text_surf, (200, i * 40 + 100))
                pygame.display.update()
                time.sleep(1.5)  # 1.5
                current_background = backgrounds[4]
                day3 = True
                option_choose = False
                option = False
                day2 = False
                player.pos_x = 100

    # Day 3 - Sep 14
    elif day3:
        screen.blit(myfont2.render("September 14", True, "black"), (400, 10))
        poster = pygame.image.load('images/poster.png')
        screen.blit(poster, (740, 400))
        # pygame.draw.rect(screen, "white", (740, 400, 140, 160))
        if not 700 - player.pos_x - 50 < 80:
            text_transparent_surface = pygame.Surface((540, 150),
                                                      pygame.SRCALPHA)
            text_transparent_surface.fill((230, 230, 230, 200))
            screen.blit(text_transparent_surface, (200, 50))
            text = [
                "What are these posters about?", "Try to come closer to see."
            ]
            for i, t in enumerate(text):
                text_surf = myfont.render(t, True, (0, 0, 0))
                screen.blit(text_surf, (220, i * 30 + 70))
            club_join = False
            pygame.display.update()
        else:
            # need to blit poster
            if not club_join:
                poster_surface = pygame.Surface((540, 250), pygame.SRCALPHA)
                poster_surface.fill((230, 230, 230, 200))
                screen.blit(poster_surface, (200, 50))
                poster_text = [
                    "Student clubs and organizations in KBTU:",
                    "1. Big City Lights",
                    "2. Crystal",
                    "3. StudEx",
                    "4. ArtHouse",
                    "5. StartUp Incubator"
                ]
                for i, j in enumerate(poster_text):
                    text_surf = myfont.render(j, True, (0, 0, 0))
                    screen.blit(text_surf, (220, i * 30 + 70))

                exit_button_surf = myfont.render('x', True, 'white')
                exit_button = pygame.Rect(700, 250, 40, 40)
                exit_button.center = (722, 280)
                pygame.draw.rect(screen, (0, 0, 0), exit_button)
                screen.blit(exit_button_surf, (exit_button.x + 14, exit_button.y + 7))

                mouse_buttons = pygame.mouse.get_pressed()
                if mouse_buttons[0]:
                    mouse_pos = pygame.mouse.get_pos()
                    if exit_button.collidepoint(mouse_pos):
                        club_join = True
            if club_join:
                text_transparent_surface = pygame.Surface((540, 150),
                                                          pygame.SRCALPHA)
                text_transparent_surface.fill((230, 230, 230, 200))
                screen.blit(text_transparent_surface, (200, 50))
                text = ["Do you want to join a club?"]
                for i, t in enumerate(text):
                    text_surf = myfont.render(t, True, (0, 0, 0))
                    screen.blit(text_surf, (220, i * 30 + 70))
                option_transparent_surface = pygame.Surface((500, 50),
                                                            pygame.SRCALPHA)
                option_transparent_surface.fill((230, 230, 230, 200))
                option1_surf = myfont.render("-sure, wanna try everything", True,
                                             "black")
                option1 = pygame.Rect(200, 250, 500, 50)
                screen.blit(option_transparent_surface, (200, 250))
                screen.blit(option1_surf, (230, 262))
                option2_surf = myfont.render("-no, im good", True, "black")
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
                    screen.fill("black")
                    # text_font = pygame.font.Font('fonts/static/PixelifySans-Bold.ttf', 40)
                    if option:
                        text = [
                            "Welcome to the club, we hope you will find a lot of friends!",
                            "", "stats:", "+2 friends", "+10 happiness",
                            "-5 health"
                        ]
                        for i, t in enumerate(text):
                            text_surf = myfont.render(t, False, "white")
                            screen.blit(text_surf, (200, i * 40 + 100))
                        player.friends += 2
                        player.happiness += 10
                        player.health -= 5
                    else:
                        text = [
                            "Okay, but be careful, you must live your life to fullest."
                        ]
                        for i, t in enumerate(text):
                            text_surf = myfont.render(t, True, "white")
                            screen.blit(text_surf, (200, i * 40 + 100))
                    pygame.display.update()
                    time.sleep(1.5)  # 1.5
                    current_background = backgrounds[2]
                    option = False
                    option_choose = False
                    day4 = True
                    day3 = False
                    player.pos_x = 200

    #Day 4 - Oct 24
    elif day4:
        screen.blit(myfont2.render("October 24", True, "black"), (400, 10))
        teacher = pygame.image.load('images/characters/teacher.png')
        teacher = pygame.transform.scale(teacher, (134 * 0.6, 164*0.6))
        friend = pygame.image.load('images/characters/f1_left.png')
        friend = pygame.transform.scale(friend, (134 * 0.6, 164*0.8))
        screen.blit(teacher, (740, 280))
        screen.blit(friend, (840, player.pos_y))
        text_transparent_surface = pygame.Surface((540, 150), pygame.SRCALPHA)
        text_transparent_surface.fill((230, 230, 230, 200))
        screen.blit(text_transparent_surface, (200, 50))
        text = [
            "You are writing a midterm test on Calculus.",
            "Your friend asks for help? What do you do?"
        ]
        for i, t in enumerate(text):
            text_surf = myfont.render(t, True, (0, 0, 0))
            screen.blit(text_surf, (220, i * 30 + 70))
        option_transparent_surface = pygame.Surface((500, 50), pygame.SRCALPHA)
        option_transparent_surface.fill((230, 230, 230, 200))
        option1_surf = myfont.render("-Sure I'll help him!", True, "black")
        option1 = pygame.Rect(200, 250, 500, 50)
        screen.blit(option_transparent_surface, (200, 250))
        screen.blit(option1_surf, (230, 262))
        option2_surf = myfont.render("-Nahh, let the bro be cooked", True, "black")
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
                black_surf.fill((0, 0, 0, (i + 1) / 60 * 255))
                screen.blit(black_surf, (0, 0))
                pygame.display.update()
                clock.tick(60)  # 60
            screen.fill("black")
            # text_font = pygame.font.Font('fonts/static/PixelifySans-Bold.ttf', 80)
            if option:
                text = [
                    "You have violated the academic honesty policy!",
                    "For your action you have been expelled…..",
                    "just kidding, but try to do no more such thing!", "",
                    "stats:", "-100 respect", "-15 grades", "-15 happiness"
                ]
                for i, t in enumerate(text):
                    text_surf = myfont.render(t, False, "white")
                    screen.blit(text_surf, (200, i * 40 + 100))
                player.grades -= 15
                player.happiness -= 15
            else:
                text = [
                    "You may be not the best friend, but definitely the best student"
                ]
                for i, t in enumerate(text):
                    text_surf = myfont.render(t, True, "white")
                    screen.blit(text_surf, (200, i * 40 + 100))
            pygame.display.update()
            time.sleep(1.5)  # 1.5
            current_background = backgrounds[4]
            # day5 = True
            option_choose = False
            option = False
            day4 = False

    pygame.display.update()
    clock.tick(15)
pygame.quit()