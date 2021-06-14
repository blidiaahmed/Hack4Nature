

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import deepforest
from  joblib import load
from Hack4Nature.requests import request_image_from_service
from  Hack4Nature.tree_calculator_position import calculate_tree_positions

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
def index(latitude,longitude,service="bing"):
    if service=="bing":
        image=request_image_from_service(lat,lon,service)
    model=joblib.load("model.joblib")
    df=model.predict_image(image,return_image=False)
    annotated_image=model.predict_image(image,return_image=True)
    df=calculate_tree_positions(df)

    return {"the image": annotated_image,"the date":df}


@app.get("/predictt")
def index(image):
    model=joblib.load("model.joblib")
    df=model.predict_image(image,return_image=False)
    annotated_image=model.predict_image(image,return_image=True)
    return {"annotated_image": annotated_image,"the date":df}


