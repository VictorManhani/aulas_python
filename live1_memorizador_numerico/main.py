from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
Window.size = [300,300]

import random

class Home(BoxLayout):
    escolha = ""
    novo = False
    auxiliar = ""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_once(self.start)
        
    def start(self, evt):
        self.ids.info.text = "Pressione Novo Jogo para Iniciar!"
        self.ids.maquina.text = "Eu sou a máquina"
        
    def novo_jogo(self):
        self.ids.numero_usuario.text = ""
        self.escolha = ""
        self.novo = True
        self.auxiliar = ""
        
        self.escolha = str(int(10 * random.random()))
        self.ids.maquina.text = "Número Escolhido -> " + self.escolha
        self.ids.info.text = "Jogo iniciado!"

    def enviar(self):
        if self.novo == True:
            numero_usuario = self.ids.numero_usuario

            self.auxiliar += self.escolha
            
            if numero_usuario.text == self.auxiliar:
                print("É Igual!")
                self.escolha = str(int(10 * random.random()))
                self.ids.info.text = "Você acertou!"
                self.ids.maquina.text = "Número Escolhido -> " + self.escolha
                numero_usuario.text = ''
            else:
                print("É diferente")
                self.ids.info.text = f"Você errou! Mas acertou {len(self.auxiliar) - 1}"
                self.ids.maquina.text = "Foi um prazer brincar com você"
                numero_usuario.text = ''
                self.novo = False

class MainApp(App):
    title = "Memorizador Numérico"

    def build(self):
        return Builder.load_string("""
Home:
    orientation: "vertical"
    padding: 30
    spacing: 10
    Label:
        id: info
    Label:
        id: maquina
    TextInput:
        id: numero_usuario
        hint_text: "Resposta"
    BoxLayout:
        orientation: "horizontal"
        Button:
            text: "Novo Jogo"
            on_release:
                root.novo_jogo()
        Button:
            text: "Enviar"
            on_release:
                root.enviar()
""")

MainApp().run()