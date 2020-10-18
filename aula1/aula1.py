# 1º maneira
# from kivy.base import runTouchApp
# from kivy.uix.button import Button
# runTouchApp(Button(text = "Hello World Kivy"))

# 2º maneira
from kivy.app import App
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        return Button(text = "Hello World Kivy 2")

MainApp().run()