from kivy.uix.popup import Popup
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatButton


class FunctionsCase:
    """
    Classe com funções usadas frequentemente no sistema
    """

    def popup_preenchimento():
        # Pop-up de erro de preenchimento
        content = MDBoxLayout(orientation="vertical", padding="10dp")
        label = MDLabel(text="Preencha devidamente todos os campos", halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf")
        close_button = MDFillRoundFlatButton(text="Fechar", size_hint=(1, None), font_name="app/support/fonts/monofonto.otf")

        content.add_widget(label)
        content.add_widget(close_button)

        popup = Popup(title="Erro", content=content, size_hint=(0.8, 0.5), auto_dismiss=False)
        close_button.bind(on_release=popup.dismiss)
        popup.open()

    def show_about():
        # Pop-up de informações sobre o sistema
        content = MDBoxLayout(orientation="vertical", padding="10dp")
        label = MDLabel(text="O idioma falado é para quem deseja se comunicar, o idioma destino é para quem for ouvir você falar.", halign="center", font_size="15dp", font_name="app/support/fonts/monofonto.otf")
        close_button = MDFillRoundFlatButton(text="Fechar", size_hint=(1, None), font_name="app/support/fonts/monofonto.otf")

        content.add_widget(label)
        content.add_widget(close_button)

        popup = Popup(title="Informações de usabilidade", content=content, size_hint=(0.8, 0.5), auto_dismiss=False)
        close_button.bind(on_release=popup.dismiss)
        popup.open()