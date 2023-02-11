import pygame

clock = pygame.time.Clock()

pygame.init()

screen = pygame.display.set_mode((900, 600)) #, flags = pygame.NOFRAME) /// убирание рамки
pygame.display.set_caption("Тест")
icon = pygame.image.load("Images/169918_infinity_loop_icon.png")
pygame.display.set_icon(icon)

bg = pygame.image.load("Images/fone.png")

walk_right = [
pygame.image.load("Images/Heroes/Right/image_part_144.png"),
pygame.image.load("Images/Heroes/Right/image_part_145.png"),
pygame.image.load("Images/Heroes/Right/image_part_146.png"),
pygame.image.load("Images/Heroes/Right/image_part_147.png"),
pygame.image.load("Images/Heroes/Right/image_part_148.png"),
pygame.image.load("Images/Heroes/Right/image_part_149.png"),
pygame.image.load("Images/Heroes/Right/image_part_150.png"),
pygame.image.load("Images/Heroes/Right/image_part_151.png"),
pygame.image.load("Images/Heroes/Right/image_part_152.png"),
]

walk_left = [
pygame.image.load("Images/Heroes/Left/image_part_118.png"),
pygame.image.load("Images/Heroes/Left/image_part_119.png"),
pygame.image.load("Images/Heroes/Left/image_part_120.png"),
pygame.image.load("Images/Heroes/Left/image_part_121.png"),
pygame.image.load("Images/Heroes/Left/image_part_122.png"),
pygame.image.load("Images/Heroes/Left/image_part_123.png"),
pygame.image.load("Images/Heroes/Left/image_part_124.png"),
pygame.image.load("Images/Heroes/Left/image_part_125.png"),
pygame.image.load("Images/Heroes/Left/image_part_126.png"),
]

player_anim_count = 0
bg_x = 0

player_speed = 5
player_x = 100
player_y = 490

is_jump = False
jump_count = 6

bg_sound = pygame.mixer.Sound('Sounds/Action 3 (Loop).mp3')
bg_sound.play()

running = True
while running:

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 900, 0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        screen.blit(walk_left[player_anim_count], (player_x, player_y))
    else:
        screen.blit(walk_right[player_anim_count], (player_x, player_y))

    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT]  and player_x < 870:
        player_x += player_speed

    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -6:
            if jump_count > 0:
                player_y -= (jump_count ** 2) / 2
            else:
                player_y += (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 6

    if player_anim_count == 8:
        player_anim_count = 0
    else:
        player_anim_count += 1
    #screen.blit(walk_right[player_anim_count], (0,490))

    bg_x -= 5
    if bg_x == -900:
        bg_x = 0

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # обработка кнопки выхода
            running = False
            pygame.quit()
    clock.tick(20)




#screen.fill((20, 70, 186)) /// cмена цвета экрана

    #if event.type == pygame.KEYDOWN: /// проверка кнопка вниз или нет
    #    if event.key == pygame.K_LCTRL: /// указание какую кнопку смотреть

# pygame.draw.circle(screen, 'Green', (0, 0), 20)
# squre = pygame.Surface((50, 170))
# squre.fill('Red')

# myfont = pygame.font.Font('Fonts/beer-money12.ttf', 40) # установка шрифта
# text_surface = myfont.render('Я работаю!', False, 'Red') # текст - сглаживание - цвет (можно кортеж RGB)

