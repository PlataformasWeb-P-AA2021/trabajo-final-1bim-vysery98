''' 
CONSULTA 2.
    * Las parroquias que tienen establecimientos únicamente en la jornada Nocturna
    * Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# Operador a emplear
from sqlalchemy import or_

# Importación de las Clases que corresponden a las entidades de la base de datos
from genera_tablas import Establecimiento, Parroquia, Canton, Provincia

# Importación del archivo de configuración
from configuracion import cadena_db

# Generación de enlace al gestor BD
engine = create_engine(cadena_db)

# Sentencias para permitir realizar operaciones a la Base de Datos
Session = sessionmaker(bind=engine)
session = Session()

# Consulta realizada a la entidad Establecimiento mediante query, se emplea join para combinar los registros de entidades a las que
# se deberá acceder y finalmente el filter para indicar que solo se desea los valores de Nocturna para la jornada.
query = session.query(Parroquia).join(Establecimiento).filter(Establecimiento.jornada == "Nocturna").all()
# Consulta realizada a la entidad Canton mediante query, se emplea join para combinar los registros de entidades a las que
# se deberá acceder y finalmente el filter para indicar que solo se desea los valores 448, 450, 451, 454, 458, 459 de num de estudiantes.
query2 = session.query(Canton).join(Parroquia, Establecimiento).filter(or_(Establecimiento.numEstud == 448, Establecimiento.numEstud == 450,
        	Establecimiento.numEstud == 451, Establecimiento.numEstud == 454, Establecimiento.numEstud == 458,Establecimiento.numEstud == 459)).all()
 
# SALIDA
cadena = "Parroquias que tienen establecimientos únicamente en la jornada Nocturna\n"
for i in query:
    cadena += "%s%s" % (cadena, i)

cadena += "%s\n\nCantones que tienen establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459\n" % (cadena)
for i in query2: 
    cadena += "%s%s" % (cadena, i)

print(cadena)
