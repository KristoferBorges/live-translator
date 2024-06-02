from kivymd.uix.screen import MDScreen
import speech_recognition as sr
from gtts import gTTS
from pygame import mixer
from googletrans import Translator
from app.support.setup import Setup
import traceback

class Traducao(MDScreen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.idioma_falado = None
        self.idioma_falado_fonte = None
        self.idioma_falado_texto = None
        self.idioma_destino = None
        self.idioma_destino_fonte = None
        self.idioma_destino_texto = None
        

    def ativandoCapturaDeVoz(self, language, translateLanguage, fonte, fonte_traducao):
        """
        Função responsável por coletar os dados do usuário por via de Voz.
        """
        while True:
            # Crie um objeto de reconhecimento de fala
            r = sr.Recognizer()

            # Use o microfone como fonte de áudio
            with sr.Microphone() as source:
                print(f"Diga algo [{language}]: ")
                audio = r.listen(source)

            try:
                # Reconheça o áudio usando o Google Speech Recognition
                texto = r.recognize_google(audio, language=language)

                if texto == "sair" or texto == "exit" or texto == "salir" or texto == "外出する" or texto == "외출하다":
                    # Implementar a saída
                    print("saida não programada")
                    
                else:
                    translator = Translator()
                    translatedText = translator.translate(texto, src=fonte, dest=fonte_traducao)
                    print(f"Texto traduzido: {translatedText.text}")
                    mixer.init()

                    audio = gTTS(
                        text=translatedText.text,
                        lang=translateLanguage,
                    )

                    audio.save("app\\support\\media\\voiceArchive\\audio_capture.mp3")
                    mixer.music.load("app\\support\\media\\voiceArchive\\audio_capture.mp3")
                    mixer.music.play()

                    while mixer.music.get_busy():
                        pass
                    
                    mixer.quit()
            
            except sr.UnknownValueError:
                print("[!] - AUDIO NÃO DETECTADO, DESEJA SAIR? [S/N]")
                if str(input("\n--> ")).upper() == "S":
                    # Implementar a saída
                    print("saida não programada")
                else:
                    continue
            
            except sr.RequestError as e:
                print("Erro ao solicitar resultados do serviço de reconhecimento de fala do Google; {0}".format(e))
            
            except Exception as _:
                # Gerando log de erro
                setup = Setup()
                erro_detalhado = traceback.format_exc()
                arquivo = open(setup.caminho_log + "log.log", "w")
                arquivo.write(str(erro_detalhado))
                arquivo.close()

    def coletaDeIdiomas(self):
        tela_principal = self.manager.get_screen("tela_principal")
        self.idioma_falado = tela_principal.idioma_falado
        self.idioma_falado_fonte = tela_principal.idioma_falado_fonte
        self.idioma_falado_texto = tela_principal.idioma_falado_texto
        self.idioma_destino = tela_principal.idioma_destino
        self.idioma_destino_fonte = tela_principal.idioma_destino_fonte
        self.idioma_destino_texto = tela_principal.idioma_destino_texto

        # mostrando na tela
        print(self.idioma_falado)
        print(self.idioma_falado_fonte)
        print(self.idioma_destino)
        print(self.idioma_destino_fonte)
        
        self.ids.idioma_primario.text = self.idioma_falado_texto
        self.ids.idioma_secundario.text = self.idioma_destino_texto

        

    def resetandoVariaveis(self):
        tela_principal = self.manager.get_screen("tela_principal")
        tela_principal.idioma_falado = None
        tela_principal.idioma_falado_fonte = None
        tela_principal.idioma_destino = None
        tela_principal.idioma_destino_fonte = None

    def ativarMicrofone(self):
        return self.ativandoCapturaDeVoz(self.idioma_falado, self.idioma_destino, self.idioma_falado_fonte, self.idioma_destino_fonte)
    
    def desativarMicrofone(self):
        mixer.quit()
        self.resetandoVariaveis()
        self.manager.current = "tela_principal"

