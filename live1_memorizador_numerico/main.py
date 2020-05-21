from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
Window.size = [300, 300]

import random

class Home(BoxLayout):
    escolha = ''
    novo = False
    aux = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_once(self.start)

    def start(self, evt):
        self.ids.info.text = 'Clique em novo jogo para começar!'
        self.ids.maquina.text = 'Aparecerá os números aqui!!'

    def verificar(self):
        if self.novo == True:
            usuario = self.ids.usuario.text

            if usuario == self.aux:
                self.escolha = str(int(10 * random.random()))
                self.aux = self.aux + self.escolha
                self.ids.maquina.text = 'Número Escolhido -> %s' % self.escolha
                self.ids.usuario.text = ''
            else:
                self.ids.info.text = f"""\
Game Over! :(
Você conseguiu {len(self.aux) - 1} pontos! \\0/
"""
                self.ids.maquina.text = ""
                self.novo = False
        else:
            self.ids.info.text = 'Clique em novo jogo para começar!'

    def novo_jogo(self):
        self.ids.usuario.text = ''
        self.escolha = ''
        self.aux = ''
        self.novo = True

        self.escolha = str(int(10 * random.random()))
        self.aux = self.escolha
        self.ids.info.text = f"Novo Jogo, boa sorte memorizador!"
        self.ids.maquina.text = f"Número Escolhido -> {self.escolha}"

class MainApp(App):
    title = "Memorizador Numérico"

    def build(self):
        return Builder.load_string("""
Home:
    orientation = 'vertical'
    padding: dp(50)
    spacing: dp(10)
    Label:
        id: info
    Label:
        id: maquina
    TextInput:
        id: usuario
        hint_text: "Resposta"
    BoxLayout:
        Button:
            text: "Novo Jogo"
            on_release:
                root.novo_jogo()
        Button:
            text: "Enviar"
            on_release:
                root.verificar()
""")

MainApp().run()