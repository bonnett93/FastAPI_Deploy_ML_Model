from pydantic import BaseModel


class Car(BaseModel):
    """Car Class"""
    Year: int
    Present_Price: int
    Kms_Driven: int
    Owner: int
    Fuel_Type_Diesel: int
    Fuel_Type_Petrol: int
    Seller_Type_Individual: int
    Transmission_Manual: int
