from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_db
from genera_tablas import Establecimiento, Canton, Parroquia, Provincia

import pandas as pd

engine = create_engine(cadena_db)

Session = sessionmaker(bind=engine)
session = Session()

dataC = pd.read_csv('data/Listado-Instituciones-Educativas.csv',sep = '|')
dataC = dataC.iloc[:,[2,4,5]].drop_duplicates()
dataC = dataC.values.tolist()

for i in dataC:
    canton = Canton(id = i[1], nameCanton = i[2], provincia = session.query(Provincia).filter_by(id = i[0]).one())

    session.add(canton)

# Confirmar transacciones
session.commit()
