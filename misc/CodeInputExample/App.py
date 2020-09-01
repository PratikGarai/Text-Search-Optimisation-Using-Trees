from kivy.app import App
from kivy.uix.codeinput import CodeInput
from kivy.extras.highlight import KivyLexer
from pygments.lexers import *
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout

class CodeSection(RelativeLayout):
    def __init__(self, **kwargs):
        super(CodeSection, self).__init__(**kwargs)
        self.section = CodeInput(lexer = PythonLexer())
        self.add_widget(self.section)

class UpperSection(RelativeLayout):
    def __init__(self, **kwargs):
        super(UpperSection, self).__init__(**kwargs)

        self.spinner = Spinner(
                text = 'Python',
                values = ('Kivy', 'Python', 'Java', 'C++'),
                size_hint = (None, None),
                size = (100,40),
                pos_hint={'center_x': .5, 'center_y': .5})
        self.add_widget(self.spinner)

        self.pos_hint = {'x':0, 'y':0}
        self.size_hint = (1,0.1)

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.u = UpperSection()
        self.c = CodeSection()
        self.add_widget(self.u)
        self.add_widget(self.c)
        self.setup()

    def change_lexer(self, spinner, text):
        if text=='Kivy':
            self.c.section.lexer = KivyLexer(tabsize = 4)
        elif text=='Python':
            self.c.section.lexer = PythonLexer(tabsize = 4)
        elif text=='Java':
            self.c.section.lexer = JavaLexer(tabsize = 4)
        elif text=='C++':
            self.c.section.lexer = CppLexer(tabsize=4)

    def setup(self):
        self.u.spinner.bind(text=self.change_lexer)

class MainApp(App):
    def build(self):
        return MainLayout()

if __name__=='__main__':
    MainApp().run()
