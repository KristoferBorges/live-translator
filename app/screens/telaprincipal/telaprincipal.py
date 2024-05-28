from kivymd.uix.screen import MDScreen
from app.support.modulo import FunctionsCase
from kivy.uix.popup import Popup
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatButton

class TelaPrincipal(MDScreen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.idioma_falado = None
        self.idioma_falado_fonte = None
        self.idioma_falado_texto = None
        self.idioma_destino = None
        self.idioma_destino_fonte = None
        self.idioma_destino_texto = None


    def definirIdiomaFalado(self, idioma_falado, idioma_texto_falado):
        self.idioma_falado = idioma_falado
        self.idioma_falado_fonte = idioma_falado[:2]
        self.idioma_falado_texto = idioma_texto_falado

        if self.idioma_falado == "pt-br":
            self.ids.btn_idioma_falado_portugues_br.md_bg_color = [.1, .4, .7, 0.90]
            self.ids.btn_idioma_falado_ingles_us.md_bg_color = [.0, .4, .2, 0.90]
        
        if self.idioma_falado == "en-us":
            self.ids.btn_idioma_falado_portugues_br.md_bg_color = [.0, .4, .2, 0.90]
            self.ids.btn_idioma_falado_ingles_us.md_bg_color = [.1, .4, .7, 0.90]

        # adicionar outros idiomas

        self.liberarBotaoTraduzir()

    def definirIdiomaDestino(self, idioma_destino, idioma_texto_destino):
        self.idioma_destino = idioma_destino
        self.idioma_destino_fonte = idioma_destino[:2]
        self.idioma_destino_texto = idioma_texto_destino

        if self.idioma_destino == "pt-br":
            self.ids.btn_idioma_destino_portugues_br.md_bg_color = [.1, .4, .7, 0.90]
            self.ids.btn_idioma_destino_ingles_us.md_bg_color = [.0, .4, .2, 0.90]
        
        if self.idioma_destino == "en-us":
            self.ids.btn_idioma_destino_portugues_br.md_bg_color = [.0, .4, .2, 0.90]
            self.ids.btn_idioma_destino_ingles_us.md_bg_color = [.1, .4, .7, 0.90]

        # adicionar outros idiomas

        self.liberarBotaoTraduzir()

    def liberarBotaoTraduzir(self):
        if self.idioma_falado != None and self.idioma_destino != None:
            self.ids.btn_iniciar.md_bg_color = [.1, .4, .7, 0.90]
            self.ids.btn_iniciar.disabled = False
        

    def verificadorDeInputs(self):
        if self.idioma_falado is None or self.idioma_destino is None:
            FunctionsCase.popup_preenchimento()
        else:
            # Idiomas falados
            self.ids.btn_idioma_falado_portugues_br.md_bg_color = [.0, .4, .2, 0.90]
            self.ids.btn_idioma_falado_ingles_us.md_bg_color = [.0, .4, .2, 0.90]

            # Idiomas destino
            self.ids.btn_idioma_destino_portugues_br.md_bg_color = [.0, .4, .2, 0.90]
            self.ids.btn_idioma_destino_ingles_us.md_bg_color = [.0, .4, .2, 0.90]

            # adicionar outros idiomas

            self.ids.btn_iniciar.md_bg_color = [.1, .4, .7, 0.20]
            self.ids.btn_iniciar.disabled = True

            # Acessando a tela de tradução e coletando os idiomas
            tela_traducao= self.manager.get_screen("tela_traducao")
            tela_traducao.coletaDeIdiomas()
            self.manager.current = "tela_traducao"

    def show_about(self):
        # Pop-up de informações sobre o sistema
        content = MDBoxLayout(orientation="vertical", padding="10dp")
        label = MDLabel(text="Idioma falado: é para quem deseja se comunicar,\nIdioma destino é para quem for ouvir você falar.\n\nIMPORTANTE: Selecione os dois idiomas para prosseguir", halign="center", font_size="25dp", font_name="app/support/fonts/monofonto.otf")
        close_button = MDFillRoundFlatButton(text="Fechar", size_hint=(1, None), font_name="app/support/fonts/monofonto.otf")

        content.add_widget(label)
        content.add_widget(close_button)

        popup = Popup(title="Informações de usabilidade", content=content, size_hint=(0.8, 0.6), auto_dismiss=False)
        close_button.bind(on_release=popup.dismiss)
        popup.open()
    
    