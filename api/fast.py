

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import deepforest
from  joblib import load
from Hack4Nature.requests.lib import request_image_from_service,generate_local_file
from  Hack4Nature.tree_calculator_position.lib import calculate_tree_positions
from PIL import Image
import numpy as np
from io import BytesIO



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
    return {"greeting": "Hello nature1"}


@app.get("/predict_dataframe_image")
def index(latitude,longitude,service="bing"):
    if service=="bing":
        response = request_image_from_service(float(latitude),float(longitude), service)
        img = Image.open(BytesIO(response.content)).convert('RGB')
        for_model = np.array(img).astype('float32')
        #image=request_image_from_service(float(latitude),float(longitude),service)
        #print(type(image))
    model=load("model.joblib")
    df=model.predict_image(for_model,return_plot =False)
    annotated_image=model.predict_image(for_model,return_plot =True)
    return { "data":df,"image":annotated_image.tolist()}


@app.get("/predict")
def index(image):
    model=load("model.joblib")
    df=model.predict_image(image,return_plot =False)
    annotated_image=model.predict_image(image,return_plot =True)
    return {"annotated_image": annotated_image,"the date":df}



