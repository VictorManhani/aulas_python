from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton

class MainApp(MDApp):
    def build(self):
        return MDIconButton(
            size_hint = [1,1],
            icon = "language-python",
            user_font_size = "64sp",
            theme_text_color = "Custom",
            text_color = self.theme_cls.primary_color
        )

MainApp().run()