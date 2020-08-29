from kivy.app import App
from kivy.uix.codeinput import CodeInput
from kivy.extras.highlight import KivyLexer
from pygments.lexers import *
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout

class CodeSection(RelativeLayout):
    def __init__(self, **kwargs):
        super(CodeSection, self).__init__(**kwargs)
        self.pos_hint = {'x':0, 'y':0}
        self.size_hint = (1,0.9)
        self.add_widget(CodeInput(lexer = KivyLexer()))

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(CodeSection())

class MainApp(App):
    def build(self):
        return MainLayout()

if __name__=='__main__':
    MainApp().run()
