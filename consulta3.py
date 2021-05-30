''' 
CONSULTA 3.
    * Los cantones que tiene establecimientos con 0 número de profesores
    * Los establecimientos que pertenecen a la parroquia Catacocha con estudiantes mayores o iguales a 21
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Importación de las Clases que corresponden a las entidades de la base de datos
from genera_tablas import Establecimiento, Parroquia, Canton, Provincia

# Importación del archivo de configuración
from configuracion import cadena_db

# Generación de enlace al gestor BD
engine = create_engine(cadena_db)

# Sentencias para permitir realizar operaciones a la Base de Datos
Session = sessionmaker(bind=engine)
session = Session()

# Consulta realizada a la entidad Canton mediante query, se emplea join para combinar los registros de entidades a las que
# se deberá acceder, filter para indicar que solo se desea los valores de 0 de número de docente.
query = session.query(Canton).join(Parroquia,Establecimiento).filter(Establecimiento.numDocentes == 0).all()
# Consulta realizada a la entidad Parroquia mediante query, se emplea join para combinar los registros de entidades a las que
# se deberá acceder y finalmente el filter para indicar que solo se desea de Catacocha y tenga más de 21 estudiantes
query2 = session.query(Establecimiento).join(Parroquia).filter(Parroquia.nameParroquia == "CATACOCHA",
            Establecimiento.numEstud >= 21).all()
 
# SALIDA
cadena = "Cantones con establecimientos de 0 profesores\n"
for i in query:
    cadena += "%s%s" % (cadena, i)

cadena += "%s\n\nEstablecimientos que pertenecen a la parroquia Catacocha con estudiantes mayores o iguales a 21\n" % (cadena)
for i in query2: 
    cadena += "%s%s" % (cadena, i)

print(cadena)
