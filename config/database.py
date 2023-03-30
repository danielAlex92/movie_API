import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#Se guardará el nombre de la base de datos
sqlite_file_name = "../database.sqlite"
#Se leerá el directorio actual del archivo database
base_dir = os.path.dirname(os.path.realpath(__file__))
# sqlite:/// es la forma en la que se conecta a una base de datos, se usa el metodo join para unir las urls
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"
# representa el motor de la base de datos, con el comando “echo=True” para que al momento de realizar la base de datos,
#me muestre por consola lo que esta realizando
engine = create_engine(database_url, echo=True)
# Se crea session para conectarse a la base de datos, se enlaza con el comando “bind” y se iguala a engine
Session = sessionmaker(bind=engine)

# Base sirve para manipular las tablas
Base = declarative_base()