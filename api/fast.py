

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import deepforest


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)



@app.get("/")
def index():
    return {"greeting": "Hello nature"}


@app.get("/predict")
def index(v1):

    return {"greeting": float(v1)+1}