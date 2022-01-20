import pygame
from pygame.sprite import Group  # подключаем из модуля  pygame.sprite класс group
import controls
from gun import Gun
from stats  import Stats
from score import Scores
from bullet import Sound


def run():
    #clock = pygame.time.Clock()
    FPS =60

    pygame.init()
    screen = pygame.display.set_mode((700,800))
    pygame.display.set_caption("Космические защитники")

    gun = Gun(screen)   # пушка = классу пушки, и мы ее добавляем  на наш графический объект

    bullets = Group() # создаем объект, принадлежащий классу Group
   # ino=Ino(screen)# Создаем объект на основе нашего класса Ino, и передаем наш экран# и отрисовываем его на экране в cтр 20, т.е. при обновлении нашего экрана мы должны отобразить пришельца
    # и также передаем его в функцию обновления экрана (def update) в файле controls
    inos = Group()
    controls.create_army(screen, inos )#обращаемся к модулю controls и вызываем функцию , которая создает армию (функция получает экран и пришельцев)
    stats = Stats() # stats является  экземпляром класса Stats()
    sc= Scores (screen, stats)#создаем экземпляр на базе класса Scores
    go = Gun(screen)
    background_image = pygame.image.load('image/space.jpg')
    background_image = pygame.transform.smoothscale(background_image, screen.get_size())
    sd = Sound()

    clock = pygame.time.Clock()
    pygame.mixer.music.load("sound/fon.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)




    while True:


        controls.events(screen, gun, bullets, sd) # функция, ответственная за отслеживание событий (пушки)
        if stats.run_game:
            gun.update_gun() # вызываем функцию, которая обновляет позицию пушки
            bullets.update()#отрисовываем и помещаем на экран пули

            controls.update( screen, sc,  gun, inos, bullets )
            controls.update_bullets(screen, stats, sc,  inos, bullets, sd)
            controls.update_inos(stats, screen, sc, gun, inos, bullets, sd, go)
            screen.blit(background_image, (0, 0))
            #pygame.display.flip()
            clock.tick(FPS)


run()