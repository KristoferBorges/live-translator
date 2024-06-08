from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from googletrans import Translator

def coletarDadosDeTexto(language1, language2, texto):
    """
    Função responsável por coletar os dados do usuário por via de Texto.
    """

    translator = Translator()
    translatedText = translator.translate(texto, src=language1[:2], dest=language2[:2])
    return translatedText.text

app = FastAPI()

@app.get("/api/translate")
async def get_translate(lang1='pt-br', lang2='en-br', text='Bom dia!'):
    translated_text = coletarDadosDeTexto(lang1, lang2, text)

    return translated_text

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
