import os
from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory
# from app.support.setup import Setup

class LiveApp(MDApp, App):
    """
    Classe principal do sistema, responsável por gerenciar o sistema de programação em tempo real e também gerenciar os caminho dos arquivos .kv/.py
    """
    # Fontes
    font_monofonto = os.path.join(os.getcwd(), "app/support/fonts/monofonto.otf")
    font_Troops = os.path.join(os.getcwd(), "app/support/fonts/Troops.otf")

    DEBUG = 1 # set this to 0 make live app not working

    # *.kv files to watch
    KV_FILES = {
        # ScreenManager
        os.path.join(os.getcwd(), "app/screens/screenmanager.kv"),

        # Demais screens
        os.path.join(os.getcwd(), "app/screens/loading/loading.kv"),
        os.path.join(os.getcwd(), "app/screens/telaprincipal/telaprincipal.kv"),
        os.path.join(os.getcwd(), "app/screens/traducao/traducao.kv"),
        
    }

    # class to watch from *.py files
    CLASSES = {
        # ScreenManager
        "MainScreenManager": "app.screens.screenmanager",

        # Demais screens
        "Loading": "app.screens.loading.loading",
        "TelaPrincipal": "app.screens.telaprincipal.telaprincipal",
        "Traducao": "app.screens.traducao.traducao",
        
    }

    # auto reload path
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]


    def build_app(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        # Setup()
        return Factory.MainScreenManager()


if __name__ == "__main__":
    LiveApp().run()