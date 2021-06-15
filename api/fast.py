

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import deepforest
from  joblib import load
from Hack4Nature.requests.lib import request_image_from_service,generate_local_file
from  Hack4Nature.tree_calculator_position.lib import calculate_tree_positions
from PIL import Image
import numpy as np


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


@app.get("/predict")
def index(latitude,longitude,service="bing"):
    if service=="bing":
        print(latitude,longitude,type(latitude),type(longitude))
        generate_local_file(latitude,longitude, service, destination='datas')
        image = Image.open('raw_data/bing/datas_47.645523_-122.1390_bing.png')

        #image=request_image_from_service(float(latitude),float(longitude),service)
        #print(type(image))
    
    model=load("model.joblib")
    df=model.predict_image(np.asarray(image),return_plot =False)
    annotated_image=model.predict_image(np.asarray(image),return_plot =False)
    # df=calculate_tree_positions(df)

    return {"the image": annotated_image,"the date":df}


@app.get("/predictt")
def index(image):
    model=load("model.joblib")
    df=model.predict_image(image,return_plot =False)
    annotated_image=model.predict_image(image,return_plot =True)
    return {"annotated_image": annotated_image,"the date":df}



