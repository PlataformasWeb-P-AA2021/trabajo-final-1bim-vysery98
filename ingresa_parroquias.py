from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_db
from genera_tablas import Establecimiento, Canton, Parroquia, Provincia

import pandas as pd

engine = create_engine(cadena_db)

Session = sessionmaker(bind=engine)
session = Session()

dataPa = pd.read_csv('data/Listado-Instituciones-Educativas.csv',sep = '|')
dataPa = dataPa.iloc[:,[4,6,7]].drop_duplicates()
dataPa = dataPa.values.tolist()

for i in dataPa:
    parroquia = Parroquia(id = i[1], nameParroquia = i[2], canton = session.query(Canton).filter_by(id = i[0]).one())
    session.add(parroquia)

# Confirmar transacciones
session.commit()
