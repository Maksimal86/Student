
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2' #  для устранения ошибки с open GL
from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from  kivy.uix.widget import Widget # для создания пустого места

from kivy.uix.button  import Button # для создания кнопки



from kivy.config import Config

Config.set('graphics', 'resizable', '0')

class  BoxApp(App): # имя класса должно заканчиваться на "App"
    def build(self): # обязательно надо создать метод с именем "build"
        '''
        bl = BoxLayout(orientation = 'horizontal', padding = [0, 25, 50, 0 ], spacing = 100 )# выставляем ориентацию кнопок, расстояние между кнопками и сторонами окна и расстояние между кнопками
        bl.add_widget(Button(text ='кнопка1'))
        bl.add_widget(Button(text='кнопка2'))
        bl.add_widget(Button(text='кнопка3'))
        gl = GridLayout(cols = 10, rows = 6, padding =[30], spacing = [20])
        for x in range(60):
            gl.add_widget(Button(text=str(x)))
        an = AnchorLayout(anchor_x = 'left', anchor_y = 'top')
        an.add_widget(Button(text='кнопкаfff', size_hint = [.5, .5]))

        #return bl
        #return gl
        return an

        '''
        '''
       # делаем форму для регистрации
        an = AnchorLayout()
        #bl = BoxLayout(orientation = 'vertical', size_hint= [.5,.5,]) - плавающий размер окна регистрации
        bl = BoxLayout(orientation='vertical', size_hint=[None, None ], size = [300, 200]) # фиксированный размер окна
        bl.add_widget(TextInput())
        bl.add_widget(TextInput())
        bl.add_widget(Button(text = 'войти'))
        an.add_widget(bl)
        return an
        '''
        gl = GridLayout(cols = 4, padding =[25] )
        gl.add_widget(Button(text = '7'))
        gl.add_widget(Button(text='8'))
        gl.add_widget(Button(text='9'))
        gl.add_widget(Button(text='x'))

        gl.add_widget(Button(text='4'))
        gl.add_widget(Button(text='5'))
        gl.add_widget(Button(text='6'))
        gl.add_widget(Button(text='-'))

        gl.add_widget(Button(text='1'))
        gl.add_widget(Button(text='2'))
        gl.add_widget(Button(text='3'))
        gl.add_widget(Button(text='+'))

        gl.add_widget(Widget()   )
        gl.add_widget(Button(text='0'))
        gl.add_widget(Button(text='.'))
        gl.add_widget(Button(text='='))

        return gl





if __name__ == "__main__": # если запускать этот код напрямую, то name будет = main, если же этот код будут запускаться из другого python кода, то main будет содержать имя модуля.
# здесь мы просто удостоверяемся, что этот код был запущен напрямую из консоли
    BoxApp().run() # метод run() наследован из класса App
