''' 
CONSULTA 5.
    * Los establecimientos ordenados por nombre de parroquia que tengan más de 20 profesores y la cadena "Permanente" en tipo de educación.
    * Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D02.
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# Operador a emplear
from sqlalchemy import and_

# Importación de las Clases que corresponden a las entidades de la base de datos
from genera_tablas import Establecimiento, Parroquia, Canton, Provincia

# se importa información del archivo configuracion
from configuracion import cadena_db

# Generación de enlace al gestor BD
engine = create_engine(cadena_db)

# Sentencias para permitir realizar operaciones a la Base de Datos
Session = sessionmaker(bind=engine)
session = Session()

# Consulta realizada a la entidad Parroquia mediante query, se emplea join para combinar los registros de entidades a las que
# se deberá acceder.
query = session.query(Establecimiento).join(Parroquia).filter(and_(Establecimiento.numDocentes >=20,Establecimiento.tipoEduc.like("%Permanente%"))).order_by(Parroquia.nameParroquia).all()
query2 = session.query(Establecimiento).filter(Establecimiento.codDistrito == "11D02").order_by(Establecimiento.sostenimiento).all()
 
# SALIDA
print("Establecimientos ordenados por nombre de parroquia que tengan más de 20 profesores y la cadena 'Permanente' en tipo de educación\n")
for i in query:
    print(i)

print("\n\nEstablecimientos ordenados por sostenimiento y tengan código de distrito 11D02")
for i in query2: 
    print(i)
