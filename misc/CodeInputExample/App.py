from kivy.app import App
from kivy.uix.codeinput import CodeInput
from kivy.extras.highlight import KivyLexer
from pygments.lexers import *
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        return CodeInput(lexer=KivyLexer())

if __name__=='__main__':
    MainApp().run()
