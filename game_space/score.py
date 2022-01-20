import pygame.font
from gun import Gun # для отображения жизней
from pygame.sprite import Group# для отображения жизней
import time
time_up = 5
class Scores():# вывод игровой информации
    black = 0,0,0

    def __init__(self,screen, stats): # инициализируем подсчет очков
        self.screen = screen # подключаем наш экран
        self.screen_rect = screen.get_rect()# получаем rect от экрана
        self.stats = stats
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 30)# берем шрифт по умолчанию
        self.image_score()
        self.image_high_score()
        self.image_guns()# выводим количество  жизней


    def image_score(self): #преобразовываем текст в графическое изображение
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, None)#
                            #  рендерим шрифт в изображение, преобразовывая сперва аргумент (текст) в строку из файла stats,

        self.score_rect = self.score_img.get_rect()# создаем объект rect для нашего текущего счета
        self.score_rect.right = self.screen_rect.right - 40 #  размещаем объект в правой верхней части экрана
        self.score_rect.top = 20


    def image_high_score(self): # преобразует рекорд в графическое изображение
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, None)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top +20
    def show_score(self):
        """Вывод счета на экран"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.guns.draw(self.screen)      # группу guns помещаем на нашем объекте screen

    def image_guns(self):# количество жизней
        self.guns = Group()
        for gun_number in range((self.stats.guns_left) +1): # перебираем и выводим столько пушек, сколько жизней

            gun = Gun(self.screen)
            gun.rect.x = 15 + gun_number*(gun.rect.width-30)
            gun.rect.y = 20
            self.guns.add(gun) # созданную пушку добавляем в группу guns

    def level(self): # Отображение уровня
        self.text = self.font.render(('Уровень  ' + str(self.stats.lev)), True, self.text_color, None)
        #self.text.set_colorkey(self.black) # делаем фон текста уровня прозрачным
        self.screen.blit(self.text, (450, 20))




    def menu(self):

        self.font50 = pygame.font.SysFont(None, 50)
        self.vopros = self.font50.render(str('Еще раз? (y/n)'), True, self.text_color, None)
        self.screen.blit(self.vopros, (250, 500))

    def timer(self):
        for times in range(time_up):
            T = time_up - times

            self.font50 = pygame.font.SysFont(None, 50)
            self.times1 = self.font50.render(('(No)' ), True, self.text_color, None)
            self.times2 = self.font50.render(( str(T)), True, self.text_color, None)

            surf = pygame.Surface.copy(self.screen)# создали копию всей плоскости экрана

            self.screen.blit(self.times1, (250, 600))
            self.screen.blit(self.times2, (350, 600))
            pygame.display.update()
            self.screen.blit(surf, (0,0)) # после обновления экрана отрисовываем плоскость всего экрана заново, чтобы изменяющийся таймер отрисовывал цифры без наложений

            time.sleep(1)














       



