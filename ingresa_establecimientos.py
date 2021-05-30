from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_db
from genera_tablas import Establecimiento, Canton, Parroquia, Provincia

import pandas as pd

engine = create_engine(cadena_db)

Session = sessionmaker(bind=engine)
session = Session()

dataE = pd.read_csv('data/Listado-Instituciones-Educativas.csv',sep = '|')
dataE = dataE.iloc[:,[0,1,6,8,9,10,11,12,13,14,15]]
dataE = dataE.values.tolist()

for i in dataE:
    establecimiento = Establecimiento(codAmie = i[0], nameEstablec = i[1], codDistrito = i[3],
        sostenimiento = i[4], tipoEduc = i[5], modalidad = i[6], jornada = i[7], acceso = i[8],
        numEstud = i[9], numDocentes = i[10], parroquia = session.query(Parroquia).filter_by(id = i[2]).one())

# Confirmar transacciones
session.commit()