''' 
CONSULTA 4.
    * Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores. 
    * Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores.
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

# Consulta realizada a la entidad Establecimiento mediante query, se emplea join para combinar los registros de entidades a las que
# se deberá acceder y finalmente el filter para indicar que solo se desea que tenga más de 100 docentes, ordenados por número de estudiantes.
query = session.query(Establecimiento).filter(Establecimiento.numDocentes > 100).order_by(Establecimiento.numEstud).all()
# Consulta realizada a la entidad Establecimiento mediante query, se emplea join para combinar los registros de entidades a las que
# se deberá acceder y finalmente el filter para indicar que solo se desea que tenga más de 100 docentes, ordenados por número de profesores.
query2 = session.query(Establecimiento).filter(Establecimiento.num_docentes > 100).order_by(Establecimiento.num_docentes).all()
 
# SALIDA
cadena = "Establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores\n"
for i in query:
    cadena += "%s%s" % (cadena, i)

cadena += "%s\n\nEstablecimientos ordenados por número de profesores; que tengan más de 100 profesores" % (cadena)
for i in query2: 
    cadena += "%s%s" % (cadena, i)

print(cadena)