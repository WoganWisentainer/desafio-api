from fastapi import FastAPI
from datetime import date
import requests

app = FastAPI()

URL_EXTERNA = "https://testedefensoriapr.pythonanywhere.com/precos"


@app.get("/precos")
def obter_precos(data: date):

    resposta = requests.get(URL_EXTERNA)

    return {
        "data": str(data),
        "precos": resposta.json()
    }