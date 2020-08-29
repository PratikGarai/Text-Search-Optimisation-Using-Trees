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
        self.add_widget(CodeInput(lexer = KivyLexer()))

class UpperSection(RelativeLayout):
    def __init__(self, **kwargs):
        super(UpperSection, self).__init__(**kwargs)

        dropdown = DropDown()
        dropdown.add_widget(Button(text="1" , size_hint_y=None , height=20))
        dropdown.add_widget(Button(text="2" , size_hint_y=None , height=20))
        dropdown.add_widget(Button(text="3" , size_hint_y=None , height=20))
        dropdown.add_widget(Button(text="4" , size_hint_y=None , height=20))

        MainButton = Button(text = "Open Dropdown")
        MainButton.bind(on_release = dropdown.open)
        
        self.add_widget(MainButton)
        self.add_widget(dropdown)

        self.pos_hint = {'x':0, 'y':0}
        self.size_hint = (1,0.1)

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(UpperSection())
        self.add_widget(CodeSection())

class MainApp(App):
    def build(self):
        return MainLayout()

if __name__=='__main__':
    MainApp().run()
