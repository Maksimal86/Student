import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2' #  для устранения ошибки с open GL

from kivy.config import Config  # Задаем размер и делаем окно неизменяемым
Config.set("graphics", "resizable", 0)
Config.set("graphics", "width", 500)
Config.set("graphics", "height", 500)

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from kivy.uix.boxlayout import BoxLayout
from pygments.lexers import HtmlLexer
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter




class MyApp(App):
    def build(self):
        s = Scatter()
        fl = FloatLayout(size = (700,200))
        s.add_widget(fl)
        fl.add_widget((Button(text = 'This is my first button',
                      font_size=30,
                      on_press = self.btn_press,
                      background_color = [.16,.16,.14,1],
                      background_normal = '',
                      size_hint = (.5, .25),
                      pos = (10,10))))
        #root = BoxLayout(orientation="vertical")
        #button = Button()
        #root.add_widget(button)
        codeinput = CodeInput(lexer = HtmlLexer())
        #root.add_widget(codeinput)
        #return root
        return s

    def btn_press(self, instance):
        print('the button was clicked')
        instance.text = 'I was cliked'


if __name__ == "__main__":
    MyApp().run()