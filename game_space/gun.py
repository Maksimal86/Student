import pygame
from pygame.sprite import Sprite # для отображения  жизней импортруем sprite и  создаем группу из спрайтов
class Gun(Sprite):
    black = 0, 0, 0
    text_color = 255,13,0
    def __init__(self, screen):
        # инициализация пушки
       super(Gun, self). __init__()# подтягиваем всё, что было у родительского класса
       self.screen=screen # Получаем наш экран
       self.image1 = pygame.image.load('image/gun.png')
       self.image1.set_colorkey(self.black)
       self.image = pygame.transform.scale(self.image1, (self.image1.get_width() // 2, self.image1.get_height() // 2))
       self.rect = self.image1.get_rect() # получаем нашу пушку как прямоугольник

       self.screen_rect = screen.get_rect() # при помощи метода get.rect()
       self.rect.centerx = self.screen_rect.centerx # координата х нашей пушки будет точно по центру графического объекта
       self.center =float(self.rect.centerx)
       self.rect.bottom= self.screen_rect.bottom # координата  низа нашей пушки
       self.mright=False
       self.mleft=False
    def output(self):
        # отрисовка пушки
        self.screen.blit(self.image1, self.rect)

    def update_gun(self):
        '''обновление позиции пушки'''
        if self.mright and self.rect.right < self.screen_rect.right:  #если  нажата клавиша, ответственная за перемещение пушки вправо,  и координата правого края пушки  х меньше, чем координата х края экрана
            self.center +=3.5   #  перемещаем пушку вправо
        if self.mleft and self.rect.left > 0:  #если  нажата клавиша, ответственная за перемещение пушки влево,  и координата левого края пушки  х больше, чем координата х края экрана
            self.center -=3.5   #  перемещаем пушку влево
        self.rect.centerx = self.center #????
    def create_gun(self):# размещаем пушку по центру внизу
        self.center=self.screen_rect.centerx



    def game_over(self):

        self.font50 = pygame.font.SysFont(None, 50)
        self.GO = self.font50.render(str('GAME_OVER'), True, self.text_color, None)

        self.rect_GO = self.GO.get_rect()
        self.rect_GO.center = self.screen_rect.center
        self.screen.blit(self.GO, self.rect_GO)  # отрисовываем на экране (screen) картинку image в координатах прямоугольника rect_GO
