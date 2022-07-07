#!/usr/bin/env python3
"""main"""
import re
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
import pickle
from backend.models.car import Car
from typing import List

app = FastAPI()
templates = Jinja2Templates(directory="frontend/templates")


@app.get('/')
def home(request: Request):
    """Home page"""
    return templates.TemplateResponse('index.html', {'request': request})


@app.post('/predict_one')
async def predict_one(car_data: Car):
    """Predict data view"""
    filename = 'ML_model/linear_regresor_model.pkl'
    with open(filename, 'rb') as f:
        model = pickle.load(f)

    data = list(car_data.__dict__.values())
    make_prediction = model.predict([data])
    output = round(make_prediction[0], 2)
    return JSONResponse(content={'Car predict price': output})


@app.post('/predict_many')
async def predict_many(cars_data: List[Car]):
    """ Predict data view """
    filename = 'ML_model/linear_regresor_model.pkl'
    with open(filename, 'rb') as f:
        model = pickle.load(f)

    data = []
    for car in cars_data:
        data.append(list(car.__dict__.values()))
    make_prediction = model.predict(data)
    output = make_prediction.tolist()
    return JSONResponse(content={'Cars predict prices': output})


if __name__ == '__main__':
    uvicorn.run(app)
