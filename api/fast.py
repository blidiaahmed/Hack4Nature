from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from  joblib import load
from Hack4Nature.requests.lib import request_image_from_service
from Hack4Nature.tree_calculator_position.lib import calculate_tree_positions
from PIL import Image
import numpy as np
from io import BytesIO

from starlette.responses import StreamingResponse

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
    return {"greeting": "Hello Hack4Nature"}



@app.get("/predict_image_as_file")
async def index(latitude,longitude,service="bing"):
    if service=="bing":
        response = request_image_from_service(float(latitude),float(longitude), service)
        img = Image.open(BytesIO(response.content)).convert('RGB')
        for_model = np.array(img).astype('float32')
        model = load("model.joblib")
        image_predicted = model.predict_image(image=for_model,return_plot=True)
        annotated_image = Image.fromarray(image_predicted, 'RGB')
        b, g, r = annotated_image.split()
        annotated_image = Image.merge("RGB", (r, g, b))
        buf = BytesIO()
        annotated_image.save(buf, format='png')
        buf.seek(0)
        return StreamingResponse(buf, media_type="image/png",
                                headers={'Content-Disposition': 'inline;'})
    else:
        return {"error": "No such service"}

@app.get("/predict_global")
def index(latitude,longitude,service="bing"):
    if service=="bing":
        response = request_image_from_service(float(latitude),float(longitude), service)
        img = Image.open(BytesIO(response.content)).convert('RGB')
        for_model = np.array(img).astype('float32')

        model = load("model.joblib")
        df = model.predict_image(image=for_model,return_plot=False)
        annotated_image=model.predict_image(image=for_model,return_plot =True)
        datas = calculate_tree_positions(df, float(latitude),float(longitude), service)
        return {"data":datas,"image":annotated_image.tolist()}
    else:
        return {"error": "No such service"}

@app.get("/predict_datas")
def index(latitude,longitude,service="bing"):
    if service=="bing":
        response = request_image_from_service(float(latitude),float(longitude), service)
        img = Image.open(BytesIO(response.content)).convert('RGB')
        for_model = np.array(img).astype('float32')
        model = load("model.joblib")
        df = model.predict_image(image=for_model,return_plot=False)
        datas = calculate_tree_positions(df, float(latitude),float(longitude), service)
        return {"data":datas}
    else:
        return {"error": "No such service"}

@app.get("/predict_image")
def index(latitude,longitude,service="bing"):
    if service=="bing":
        response = request_image_from_service(float(latitude),float(longitude), service)
        img = Image.open(BytesIO(response.content)).convert('RGB')
        for_model = np.array(img).astype('float32')
        model = load("model.joblib")
        annotated_image=model.predict_image(image=for_model,return_plot =True)
        return {"image":annotated_image.tolist()}
    else:
        return {"error": "No such service"}


@app.get("/predict_image_given")
def index(image):
    model = load("model.joblib")
    df = model.predict_image(image=image,return_plot=False)
    annotated_image=model.predict_image(image=image,return_plot =True)
    
    return {"data":datas,"image":annotated_image.tolist()}
