from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_db
from genera_tablas import Establecimiento, Canton, Parroquia, Provincia

import pandas as pd

engine = create_engine(cadena_db)

Session = sessionmaker(bind=engine)
session = Session()

dataPr = pd.read_csv('data/Listado-Instituciones-Educativas.csv',sep = '|')
dataPr = dataPr.iloc[:,[2,3]].drop_duplicates()
dataPr = dataPr.values.tolist()

for i in dataPr:
    provincia = Provincia(id = i[0], nameProvincia = i[1])
    session.add(provincia)

# Confirmar transacciones
session.commit()
