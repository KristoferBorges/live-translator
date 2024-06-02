import traceback

class Setup:
    """
    Classe de configuração do sistema
    """
    def __init__(self, **kwargs):
        # Configurações do logger
        self.caminho_log = "logs/"

    def teste(self):
        try:
            print(5 / 0)
        
        except Exception as _:
            erro_detalhado = traceback.format_exc()
            arquivo = open(self.caminho_log + "log.log", "w")
            arquivo.write(str(erro_detalhado))
            arquivo.close()

Setup.teste(Setup())