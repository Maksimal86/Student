import pygame


class Bullet(pygame.sprite.Sprite): #Создаем новый класс (дочерний) основе, который уже есть в модуле sprite
    def __init__(self, screen, gun): #прописываем метод init, который будет принимать в себя экран и пушку (будем отслеживать, где в данный момент находится пушка и создавать в том месте пулю)
        super( Bullet, self).__init__() # т.к. класс дочерний - прописываем метод super, и берем всё что есть у основного класса sprite
        self.screen = screen # берем объект экрана
        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(0,0,2,20)# Создаем пулю в позиции 0,0, размером 2х12
        self.color = 255, 255, 255 # цвет
        self.speed = 5 #скорость изменения позиции y
        self.rect.centerx = gun.rect.centerx#(="положение пушки по координате х) пуля будет появлятся в верхней части пушки
        self.rect.top = gun.rect.top# прописываем верхнюю часть пушки из которой появляется пуля.

        self.y = float(self.rect.y)#

    def update(self):
        "перемещение пули вверх"
        self.y -= self.speed
        self.rect.y = self.y #обновляем позицию пули
    def draw_bullet(self):
        "Рисуем пулю на экране"
        pygame.draw.rect(self.screen, self.color, self.rect)


class Sound():
    def sound_b(self): #Звук выстрела
        new_sound = pygame.mixer.Sound("sound/laser.wav") # создали объект класса Sound
        new_sound.play() # применили метод play к экземпляру класса
        new_sound.set_volume(0.1)
    def sound_u(self): #Смена уровня b
        sound_u = pygame.mixer.Sound("sound/uroven.wav")
        sound_u.play()
    def sound_go(self): # окончание игры
        sound_go = pygame.mixer.Sound("sound/game-over.wav")
        sound_go.play()