# Quero criar um script executável capaz de receber um texto, seja uma frase, um poema ou um texto grande e transformar em áudio.
# O sistema terá a função de coleta de dados e a função de transformar o texto em áudio.
import speech_recognition as sr
from gtts import gTTS
from pygame import mixer
from googletrans import Translator

def coletarDadosDeTexto(language, translateLanguage, fonte, fonte_traducao):
    """
    Função responsável por coletar os dados do usuário por via de Texto.
    """
    while True:
        texto = input(f"Digite o texto para traduzir: [{language}]: ")
        if texto == "0":
            main()
        else:
            translator = Translator()
            translatedText = translator.translate(texto, src=fonte, dest=fonte_traducao)
            print(f"Texto traduzido: {translatedText.text}")
            mixer.init()

            audio = gTTS(
                text=translatedText.text,
                lang=translateLanguage,
            )

            audio.save("media\\voiceArchive\\audio_capture.mp3")
            mixer.music.load("media\\voiceArchive\\audio_capture.mp3")
            mixer.music.play()

            while mixer.music.get_busy():
                pass
            
            mixer.quit()

def coletarDadosDeVoz(language, translateLanguage, fonte, fonte_traducao):
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
                main()

            else:
                translator = Translator()
                translatedText = translator.translate(texto, src=fonte, dest=fonte_traducao)
                print(f"Texto traduzido: {translatedText.text}")
                mixer.init()

                audio = gTTS(
                    text=translatedText.text,
                    lang=translateLanguage,
                )

                audio.save("media\\voiceArchive\\audio_capture.mp3")
                mixer.music.load("media\\voiceArchive\\audio_capture.mp3")
                mixer.music.play()

                while mixer.music.get_busy():
                    pass
                
                mixer.quit()
        
        except sr.UnknownValueError:
            print("[!] - AUDIO NÃO DETECTADO, DESEJA SAIR? [S/N]")
            if str(input("\n--> ")).upper() == "S":
                main()
            else:
                continue

        except sr.RequestError as e:
            print("Erro ao solicitar resultados do serviço de reconhecimento de fala do Google; {0}".format(e))

def main():
    """
    Função de execução, também questiona qual método de coleta de dados o usuário deseja utilizar.
    """
    collectionMethod = str(input("\n[!] - QUAL TIPO DE COLETA\n[1] - Texto\n[2] - Voz\n--> "))
    while collectionMethod not in "12":
        collectionMethod = str(input("\n[!] - DIGITE SOMENTE AS OPÇÕES DISPONÍVEIS\n[1] - Texto\n[2] - Voz\n-->"))

    listenLanguage = str(input("\n[!] - QUAL IDIOMA VOCÊ FALA?\n[1] - Português\n[2] - Inglês\n[3] - Espanhol\n[4] - Japones\n[5] - Coreano\n[6] - Árabe \n--> "))
    while listenLanguage not in "123456":
        listenLanguage = str(input("\n[!] - DIGITE SOMENTE AS OPÇÕES DISPONÍVEIS\n[1] - Português\n[2] - Inglês\n[3] - Espanhol\n[4] - Japones\n-->\n[5] - Coreano\n[6] - Árabe \n--> "))

    translateLanguage = str(input("\n[!] - QUAL IDIOMA VOCÊ DESEJA TRADUZIR?\n[1] - Português\n[2] - Inglês\n[3] - Espanhol\n[4] - Japones\n[5] - Coreano\n[6] - Árabe \n--> "))
    while translateLanguage not in "123456":
        translateLanguage = str(input("\n[!] - DIGITE SOMENTE AS OPÇÕES DISPONÍVEIS\n[1] - Português\n[2] - Inglês\n[3] - Espanhol\n[4] - Japones\n[5] - Coreano\n[6] - Árabe \n--> "))
    
    if listenLanguage == "1":
        listenLanguage = "pt-br"
        fonte = "pt"
    elif listenLanguage == "2":
        listenLanguage = "en-us"
        fonte = "en"
    elif listenLanguage == "3":
        listenLanguage = "es"
        fonte = "es"
    elif listenLanguage == "4":
        listenLanguage = "ja"
        fonte = "ja"
    elif listenLanguage == "5":
        listenLanguage = "ko"
        fonte = "ko"
    elif listenLanguage == "6":
        listenLanguage = "ar"
        fonte = "ar"

    if translateLanguage == "1":
        translateLanguage = "pt-br"
        fonte_traducao = "pt"

    elif translateLanguage == "2":
        translateLanguage = "en-us"
        fonte_traducao = "en"

    elif translateLanguage == "3":
        translateLanguage = "es"
        fonte_traducao = "es"
    
    elif translateLanguage == "4":
        translateLanguage = "ja"
        fonte_traducao = "ja"

    elif translateLanguage == "5":
        translateLanguage = "ko"
        fonte_traducao = "ko"
    
    elif translateLanguage == "6":
        translateLanguage = "ar"
        fonte_traducao = "ar"

    if collectionMethod == "1":
        coletarDadosDeTexto(listenLanguage, translateLanguage, fonte, fonte_traducao)
    elif collectionMethod == "2":
        coletarDadosDeVoz(listenLanguage, translateLanguage, fonte, fonte_traducao)

if __name__ == "__main__":
    main()