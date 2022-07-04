#!/usr/bin/env python3
"""xlsx to mysql converter"""

from os import getenv
from sqlalchemy import create_engine
import pandas as pd

# conect to MySQL
MYSQL_USER = getenv('MYSQL_USER')
MYSQL_PWD = getenv('MYSQL_PWD')
MYSQL_HOST = "localhost"
MYSQL_DB = "FastAPI_Deploy_ML_Model"
db_conection = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(MYSQL_USER,
                                             MYSQL_PWD,
                                             MYSQL_HOST,
                                             MYSQL_DB))

# open file and read
data_frame = pd.read_excel('car_data.xlsx')
# print(df.head())
# print(df.tail())

# save as a mysql table
data_frame.to_sql(con=db_conection, name="car_data", if_exists='replace')
