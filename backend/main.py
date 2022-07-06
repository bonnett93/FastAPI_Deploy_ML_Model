#!/usr/bin/env python3
"""ML api"""
import re
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pickle

app = FastAPI()
templates = Jinja2Templates(directory="frontend/templates")


@app.get('/')
def home(request: Request):
    """Home page"""
    return templates.TemplateResponse('index.html', {'request':request})


@app.get('/predict_one')
async def predict_one(Year: str, Present_Price: str, Kms_Driven: str, Owner: str,
            Fuel_Type_Diesel: str, Fuel_Type_Petrol: str,
            Seller_Type_Individual: str, Transmission_Manual: str):
    """Predict data view"""
    filename = 'ML_model/linear_regresor_model.pkl'
    with open(filename, 'rb') as f:
        model = pickle.load(f)

    car_data = [Year, Present_Price, Kms_Driven, Owner, Fuel_Type_Diesel,
                Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Manual]
    make_prediction = model.predict([car_data])
    output = round(make_prediction[0], 2)
    return {'You can Sell Your Car for {}'.format(output)}


if __name__ == '__main__':
    uvicorn.run(app)
