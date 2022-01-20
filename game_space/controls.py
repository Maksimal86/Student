import pygame, sys
from bullet import Bullet   #импортируем класс Bullet
from ino import Ino
from gun import Gun
import time
uskor = 0.1

def events(screen, gun, bullets, sd ): # передаем в функцию events, которая обрабатывает наши события, экран, пушку  и пулю
    '''Обработка событий'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:# Если нажата клавиша ( ниже уже условие, какая именно)
            if event.key == pygame.K_RIGHT: # если отслежено событие нажатия клавиши "right"
                gun.mright =True # то присваиваем переменной значение true
            elif event.key == pygame.K_LEFT:  # если отслежено событие нажатия клавиши "left"
                gun.mleft = True  # то присваиваем переменной значение true
            elif event.key == pygame.K_SPACE:

                new_bullet = Bullet(screen, gun)#создаем новую пулю на основе класса Bullet на нашем текущем экране и,  исходя из текущей позиции  пушки
                bullets.add(new_bullet)# добавляем в контейнер bullets при помощи метода add пулю
                sd.sound_b() #применили функцию sound_b к экземпляру класса sd


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT: #  если клавиша отжата, то false
                gun.mright = False
            elif event.key == pygame.K_LEFT:  # если клавиша отжата, то false
                gun.mleft = False
            elif event.key == pygame.K_SPACE:
                bullets.space = False
def finish (sc, stats, screen, inos):
    ev = pygame.event.wait(5)
    if ev.type == pygame.KEYDOWN and ev.key == pygame.K_y:
        create_army(screen, inos)  #
        sc.image_guns()
        #time.sleep(5)
        print(str(time.sleep(5)))
        pygame.display.update()
    elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_n:
        stats.run_game = False
        sys.exit()
    else:
        stats.run_game = False
        sys.exit()

def update( screen,  sc, gun, inos, bullet):    # функция, ответственная за обновление экрана"
    #screen.fill(bg_color)

    sc.show_score() # вызываем метод отображения счета на экране сразу с начала игры
    sc.level() # отображаем уровень на экране
    for bullet in bullet.sprites():# до того как отрисовываем пушку, выводим пули (позади пушки)
        bullet.draw_bullet() # вызываем bullet и прорисовываем пули
    gun.output()  # у нашего объекта gan вызываем output, отрисовывает нашу пушку
    inos.draw(screen) # вызываем у inos метод draw, который   отрисовывает их на экране
    pygame.display.flip()
def update_bullets(screen, stats, sc, inos, bullets, sd): #обновляем позиции пуль
    bullets.update()
    global uskor
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)# применяем библиотеку pygame, в ней берем модуль sprite используем метод groupcollide, передаем группы с пулями, пришельцами
    # в этой строке перебираем группы пуль и пришельцев и, если они пересекаются, т.е. образуется коллизия, добавляем их в словарь, где ключ - пуля, значение - пришелец.
    #True и True значит, что мы удаляем и пулю и пришельца
    if collisions:
        for inos in collisions.values():
            stats.score += len(inos)   # ?????????
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_guns()# выводим жизни
    if len(inos)==0: # если уничтожили всех пришельцев

        bullets.empty() # уничтожаем все пули
        create_army(screen, inos)# создаем армию заново
        stats.lev+=1
        uskor +=0.01 # добавляем ускорение на каждом уровне
        sd.sound_u()
        time.sleep(5)

def gun_kill (stats,   screen, sc,  gun, inos, bullets, sd, go):# столкновение пушки и армии


    if stats.guns_left > 0:
        stats.guns_left -=1 # убираем одну жизнь
        sc.image_guns() # отняли жизнь, и должны заново отрисовать количество жизней
        inos.empty()# убираем всех пришельцев
        bullets.empty()#убираем все пули
        create_army(screen,inos)# заново создаем армию
        gun.create_gun()#отрисовываем заново пушку


        time.sleep(2)# задержка перед перезагрузкой\

    else:

        inos.empty()  # убираем всех пришельцев
        bullets.empty()
        go.game_over()
        sd.sound_go()
        sc.menu()
        sc.timer()
        pygame.display.update()
        time.sleep(1)
        finish(sc, stats, screen, inos)

def update_inos(stats, screen, sc, gun, inos, bullets, sd, go):# обновление позиций инопланетян
    inos.update()

    if pygame.sprite.spritecollideany(gun,inos): # проверяем перекрытие пушки и пришельцев
        gun_kill(stats, screen, sc, gun, inos, bullets, sd, go)# при столкновении пушки и пришельца вызываем функцию gun_kill
    inos_check(stats, screen, sc, gun, inos, bullets, sd, go)
def inos_check(stats, screen, sc, gun, inos, bullets, sd,go):# проверка: дошла ли армия до края экрана
    screen_rect=screen.get_rect()# получаем прямоугольник нашего экрана
    for ino in inos.sprites(): # перебираем всех пришельцев
        if ino.rect.bottom >= screen_rect.bottom:

            gun_kill(stats, screen, sc , gun, inos, bullets, sd, go)
            break # если никто не вышел за экран, то прекращаем цикл

def create_army(screen,inos): # создание армии
    ino = Ino(screen)# создаем одного пришельца
    ino_wight=ino.rect.width + 25   # расстояние между пришельцами
    number_ino_x = int(((700-ino_wight)/ino_wight))#рассчитываем - Сколько в один ряд помещается пришельцев
    ino_height = ino.rect.height+5
    number_ino_y = int((800-300-2*ino_height)/ino_height)
    first = 0
    for row_number in range(number_ino_y):#этот цикл будет создавать ряды, а в них уже будут отрисовываться пришельцы следующим циклом
        if row_number > 7:

            number_ino_x -= 1
            first += 1



        for ino_number in range(first , number_ino_x-1):
            ino=Ino(screen) #создали одного
            if row_number % 1 == 0:
                ino.x = ino_wight+ ino_wight*ino_number-5
            else:
                ino.x = ino_wight + ino_wight * ino_number
            ino.y = ino_height + ino_height*row_number + 50 # отступ от верха экрана
            ino.rect.x=ino.x  #создаем пришельцев раз за разом в каждой итерации цикла
            ino.rect.y = ino.y         #rect.height + ino.rect.height*row_number # как было
            inos.add(ino)#  добавляем каждого созданного пришельца в группу inos
            #pygame.display.update()



def check_high_score(stats, sc): # проверка новых рекордов
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('high_score.txt', 'w') as f:
            f.write(str(stats.high_score))

