import pygame
import controls

xx = 0.8
class Ino(pygame.sprite.Sprite): # класс одного пришельца

    def __init__(self,screen): # инициализируем класс и передаем ему в качестве арумента экран
        super (Ino,self).__init__()#  подтягиваем всё из родительского класса Sprite
        self.screen = screen # подтятгиваем сам экран
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load('image/11.png') # загружаем изображение
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width  # отслеживаем ширину по х
        self.rect.y = (self.rect.height)  # отслеживаем выcоту по у
        self.x = float(self.rect.x)  # отслеживаем координату х
        self.y = float(self.rect.y)  # отслеживаем координату у


    def draw(self):
        '''Вывод прищельца на экран'''
        self.screen.blit(self.image, self.rect)# обращаемся к экрану и вызываем метод blit, который будет отрисовывать,  и передаем ему изображение и выводим как прямоугольник


    def update(self): # перемещает пришельцев вниз
        global xx

        self.y += 0.09 + controls.uskor
        self.rect.y = self.y

        if self.rect.x >= 700-self.rect.width-15: #self.screen_rect.right:
            xx = -0.4
        if self.rect.x <= self.rect.width-15: # self.screen_rect.right:
            xx = 0.4
        self.x +=xx
        self.rect.x =self.x


        pygame.display.update(self)










