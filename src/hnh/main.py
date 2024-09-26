from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi import Request
from typing import Union
from transformers import pipeline
import random

app = FastAPI()


@app.get("/")
def test():
    return {"Test": "Done"}


@app.get("/predict")
def hotdog():
    model = pipeline("image-classification", model="julien-c/hotdog-not-hotdog")
    pre = ("Not Hotdog", "Hotdog")
    return random.choice(pre)
