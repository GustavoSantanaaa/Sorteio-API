import random
from fastapi import FastAPI

app = FastAPI()

ITENS = ["Ecobag", "Caneta", "Caderneta", "Kit completo"]

@app.get("/sortear")
def sortear():
    return {"item": random.choice(ITENS)}