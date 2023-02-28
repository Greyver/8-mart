import pygame
import pygame as pg

clock = pygame.time.Clock()

pygame.init()

# , flags = pygame.NOFRAME) /// убрать рамку
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Тест")
# ? используется для пнг картинок, для других форматов просто convert()
icon = pygame.image.load("Images\logo.png").convert_alpha()
pygame.display.set_icon(icon)

bg = pygame.image.load("Images\lfone.png").convert_alpha()

present = pygame.image.load("Images\present.png").convert_alpha()
present_rect = present.get_rect(topleft=(865, 375))

demon = pygame.image.load("Images\demon.jpg").convert_alpha()

walk_right = [
    pygame.image.load(
        "Images\Heroes\Right\image_part_144.png").convert_alpha(),
    pygame.image.load(
        "Images\Heroes\Right\image_part_145.png").convert_alpha(),
    pygame.image.load(
        "Images\Heroes\Right\image_part_146.png").convert_alpha(),
    pygame.image.load(
        "Images\Heroes\Right\image_part_147.png").convert_alpha(),
    pygame.image.load(
        "Images\Heroes\Right\image_part_148.png").convert_alpha(),
    pygame.image.load(
        "Images\Heroes\Right\image_part_149.png").convert_alpha(),
    pygame.image.load(
        "Images\Heroes\Right\image_part_150.png").convert_alpha(),
    pygame.image.load(
        "Images\Heroes\Right\image_part_151.png").convert_alpha(),
    pygame.image.load(
        "Images\Heroes\Right\image_part_152.png").convert_alpha(),

]

walk_left = [
    pygame.image.load(
        "Images\Heroes\Left\image_part_118.png").convert_alpha(),
    pygame.image.load(
        "Images\Heroes\Left\image_part_119.png").convert_alpha(),
    pygame.image.load(
        "Images\Heroes\Left\image_part_120.png").convert_alpha(),
    pygame.image.load(
        "Images\Heroes\Left\image_part_121.png").convert_alpha(),
    pygame.image.load(
        "Images\Heroes\Left\image_part_122.png").convert_alpha(),
    pygame.image.load(
        "Images\Heroes\Left\image_part_123.png").convert_alpha(),
    pygame.image.load(
        "Images\Heroes\Left\image_part_124.png").convert_alpha(),
    pygame.image.load(
        "Images\Heroes\Left\image_part_125.png").convert_alpha(),
    pygame.image.load(
        "Images\Heroes\Left\image_part_126.png").convert_alpha(),
]

opponent_walk_left = [
    pygame.image.load("Images\Opponent\image_part_118.png").convert_alpha(),
    pygame.image.load("Images\Opponent\image_part_119.png").convert_alpha(),
    pygame.image.load("Images\Opponent\image_part_120.png").convert_alpha(),
    pygame.image.load("Images\Opponent\image_part_121.png").convert_alpha(),
    pygame.image.load("Images\Opponent\image_part_122.png").convert_alpha(),
    pygame.image.load("Images\Opponent\image_part_123.png").convert_alpha(),
    pygame.image.load("Images\Opponent\image_part_124.png").convert_alpha(),
    pygame.image.load("Images\Opponent\image_part_125.png").convert_alpha(),
    pygame.image.load("Images\Opponent\image_part_126.png").convert_alpha(),
]

opponent = pygame.image.load(
    "Images\Opponent\image_part_118.png").convert_alpha()

opponent_list_in_game = []

player_anim_count = 0
bg_x = 0

player_speed = 5
player_x = 100
player_y = 490

opponent_timer = pygame.USEREVENT + 1
pygame.time.set_timer(opponent_timer, 1500)

is_jump = False
jump_count = 7

label = pygame.font.Font("Fonts\jbeer-money12.ttf", 60)
lose_label = label.render("YOU DIED", False, (255, 0, 0))
mart = label.render(
    "Congratulations on International Women's Day!", False, (255, 0, 0))
restart_label = label.render("RESTART", False, (0, 255, 0))
restart_label_rect = restart_label.get_rect(topleft=(350, 340))

gameplay = True

nomer_anim_vraga = 0

vusota_box = 1
flag = True

conec = False

demon_flag = True

bg_sound = pygame.mixer.Sound('Sounds\Action 3 (Loop).mp3')
bg_sound.play()
#! начало цикла screen.blit(walk_left[player_anim_count], (player_x, player_y))
running = True
while running:

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 900, 0))

    screen.blit(present, (845, 395 - vusota_box))
    if flag:
        vusota_box += 1
    if flag == False:
        vusota_box -= 1
    if vusota_box == 10:
        flag = False
    if vusota_box == 0:
        flag = True
    if gameplay:
        # ? создаються квадраты вокруг персонажей для отслеживания прикосновений
        # walk_left[0].get_rect(topleft=(player_x, player_y))
        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))
        # opponent_rect = opponent.get_rect(topleft=(opponent_x, 490))

        if opponent_list_in_game and demon_flag:
            for (i, el) in enumerate(opponent_list_in_game):
                if nomer_anim_vraga == 9:
                    nomer_anim_vraga = 0
                screen.blit(opponent_walk_left[nomer_anim_vraga], el)
                nomer_anim_vraga += 1
                el.x -= 5

                if el.x < -10:
                    opponent_list_in_game.pop(i)

                if player_rect.colliderect(el.inflate(-70, -70)):
                    print("YOU DIED:" + str(player_x))
                    gameplay = False
        if player_rect.colliderect(present_rect.inflate(50, 50)) or conec:
            screen.blit(demon, (0, 0))
            conec = True
            screen.blit(mart, (0, 520))
            demon_flag = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            screen.blit(walk_left[player_anim_count], (player_x, player_y))
        elif keys[pygame.K_RIGHT]:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))
        else:
            screen.blit(walk_right[0], (player_x, player_y))

        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 870:
            player_x += player_speed

        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump_count >= -7:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 7

        if player_anim_count == 8:
            player_anim_count = 0
        else:
            player_anim_count += 1
        # screen.blit(walk_right[player_anim_count], (0,490))

    else:
        screen.fill((0, 0, 0))
        screen.blit(lose_label, (335, 260))
        screen.blit(restart_label, restart_label_rect)

        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 100
            opponent_list_in_game.clear()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # обработка кнопки выхода
            running = False
            pygame.quit()
        if event.type == opponent_timer:
            opponent_list_in_game.append(
                # pg.Rect(910, 490, 2, 2))  # topleft=(910, 500)))
                opponent.get_rect(topleft=(910, 490)))
            # print(opponent_list_in_game[0].topleft)
    clock.tick(20)


# screen.fill((20, 70, 186)) /// cмена цвета экрана

    # if event.type == pygame.KEYDOWN: /// проверка кнопка вниз или нет
    #    if event.key == pygame.K_LCTRL: /// указание какую кнопку смотреть

# pygame.draw.circle(screen, 'Green', (0, 0), 20)
# squre = pygame.Surface((50, 170))
# squre.fill('Red')

# myfont = pygame.font.Font('Fonts/beer-money12.ttf', 40) # установка шрифта
# text_surface = myfont.render('Я работаю!', False, 'Red') # текст - сглаживание - цвет (можно кортеж RGB)
