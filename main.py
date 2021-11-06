from typing import Optional

from fastapi import FastAPI

from correios import Correios
from pyrastreio import jadlog

app = FastAPI()

correios = Correios()

@app.get("/")
def read_root():
    return { 'status': 'ok' }

@app.get("/rastreio/correios/{rastreio}")
def get_correios_tracking(rastreio: str):
    objeto = correios.rastreio(cod=rastreio)
    return objeto


@app.get("/rastreio/jadlog/{rastreio}")
def get_jadlog_tracking(rastreio: str):
    objeto = jadlog(rastreio)
    return objeto
