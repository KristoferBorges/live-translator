from kivymd.uix.screen import MDScreen

class Traducao(MDScreen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.idioma_falado = None
        self.idioma_falado_fonte = None
        self.idioma_falado_texto = None
        self.idioma_destino = None
        self.idioma_destino_fonte = None
        self.idioma_destino_texto = None

    def coletaDeIdiomas(self):
        tela_principal = self.manager.get_screen("tela_principal")
        self.idioma_falado = tela_principal.idioma_falado
        self.idioma_falado_fonte = tela_principal.idioma_falado_fonte
        self.idioma_falado_texto = tela_principal.idioma_falado_texto
        self.idioma_destino = tela_principal.idioma_destino
        self.idioma_destino_fonte = tela_principal.idioma_destino_fonte
        self.idioma_destino_texto = tela_principal.idioma_destino_texto

        self.ids.idioma_primario.text = self.idioma_falado_texto
        self.ids.idioma_secundario.text = self.idioma_destino_texto
    
    def resetandoVariaveis(self):
        tela_principal = self.manager.get_screen("tela_principal")
        tela_principal.idioma_falado = None
        tela_principal.idioma_falado_fonte = None
        tela_principal.idioma_destino = None
        tela_principal.idioma_destino_fonte = None