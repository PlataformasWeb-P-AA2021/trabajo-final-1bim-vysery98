# PROCESO DE GENERACIÓN DE ENTIDADES A TRAVÉS DE SqlAlchemy

from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql.schema import UniqueConstraint
# Importación del archivo de configuración
from configuracion import cadena_db

# Generación de enlace al gestor BD
engine = create_engine(cadena_db)
Base = declarative_base()

'''
Consideraciones a tomar en cuenta:
- Un establecimiento tiene características propias.
- Un establecimiento pertenece a una parroquia.
- Una parroquia pertence a un cantón.
- Un cantón pertence a un provincia.
'''

class Establecimiento(Base):
    __tablename__ = 'establecimiento'

    codAmie = Column(String, primary_key=True)
    nameEstablec = Column(String)
    codDistrito = Column(String)
    sostenimiento = Column(String)
    tipoEduc = Column(String)
    modalidad = Column(String)
    jornada = Column(String)
    acceso = Column(String)
    numEstud = Column(Integer)
    numDocentes = Column(Integer)
    
    '''
    Foreign Key - Un establecimiento pertenece a una parroquia
    Relación: UNO a MUCHOS
    '''
    parroquia_id = Column(Integer, ForeignKey('parroquia.id'))
    # Relación con la entidad Parroquia
    parroquia = relationship("Parroquia", back_populates="establecimientos")
    
    def __repr__(self):
        return "Código AMIE = %s\nNombre = %s\nCódigo de Distrito: %s\nSostenimiento = %s\n\
                    Tipo de Educación = %s\nModalidad = %s\nJornada(s) = %s\nVía de acceso = %s\
                    Número de Estudiantes = %d\nNúmero de Docentes = %d" % (
                        self.codAmie,
                        self.nameEstablec,
                        self.codDistrito,
                        self.sostenimiento,
                        self.tipoEduc,
                        self.modalidad,
                        self.jornada,
                        self.acceso,
                        self.numEstud,
                        self.numDocentes)

class Parroquia(Base):
    __tablename__ = 'parroquia'

    id = Column(Integer, primary_key=True)
    # Nombre de Parroquia
    nameParroquia = Column(String(50))
    
    # Relación con la entidad Establecimiento
    establecimientos = relationship("Establecimiento", 
    back_populates="parroquia")
    '''
    Foreign Key - Una parroquia pertence a un cantón
    Relación: UNO a MUCHOS
    '''
    canton_id = Column(Integer, ForeignKey('canton.id'))
    # Relación con la entidad Cantón
    canton = relationship("Canton", back_populates="parroquias")
    def __repr__(self):
        return "Código de División Política Administrativa (Parroquia) = %d\nParroquia = %s" % (
                        self.id,
                        self.nameParroquia)

class Canton(Base):
    __tablename__ = 'canton'

    id = Column(Integer, primary_key=True)
    # Nombre de Cantón
    nameCanton = Column(String(50), unique = True)
    
    # Relación con la entidad Parroquia
    parroquias = relationship("Parroquia", back_populates="canton")
    '''
    Foreign Key - Un cantón pertence a un provincia
    Relación: UNO a MUCHOS
    '''
    provincia_id = Column(Integer, ForeignKey('provincia.id'))
    # Relación con la entidad Provincia
    provincia = relationship("Provincia", back_populates="cantones")
    def __repr__(self):
        return "Código de División Política Administrativa (Cantón) = %s\nCantón = " % (
                        self.id,
                        self.nameCanton)

class Provincia(Base):
    __tablename__ = 'provincia'

    id = Column(Integer, primary_key=True)
    # Nombre de Provincia
    nameProvincia = Column(String(50), unique = True)
    
    # Relación con la entidad Cantones
    cantones = relationship("Canton", back_populates="provincia")

    def __repr__(self):
        return "Código de División Política Administrativa (Provincia) = %s\nProvincia = " % (
                        self.id,
                        self.nameProvincia)

Base.metadata.create_all(engine)
