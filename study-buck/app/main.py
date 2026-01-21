from fastapi import FastAPI
from app.api import game

app = FastAPI()

app.include_router(game.router)