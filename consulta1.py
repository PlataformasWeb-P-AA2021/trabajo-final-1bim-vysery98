''' 
CONSULTA 1.
    * Todos los establecimientos de la provincia de Loja.
    * Todos los establecimientos del cantón de Loja.
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# Operador a emplear
from sqlalchemy import and_

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
# se deberá acceder y finalmente el filter para indicar que solo se desea los valores de LOJA tanto en Provincias como Cantones.
query = session.query(Establecimiento).join(Parroquia,Canton,Provincia).filter(Provincia.nameProvincia =="LOJA").all()
query2 = session.query(Establecimiento).join(Parroquia,Canton).filter(Canton.nameCanton =="LOJA").all()
 
# SALIDA
print("Establecimientos de la provincia de Loja\n")
for i in query:
    print(i)

print("\n\nEstablecimientos del cantón Loja\n")
for i in query2: 
    print(i)
