#Archvo pricipal de la app, ejecutar este (Archivo final para el Deploy)
'''Preparamos nuestro proyecto para deploy y creamos carpeta utils donde movemos el archivo 
jwt_manager, VSCode nos pregunta que si queremos hacer una refactorizacion del codigo al mover 
este archivo, le decimos Ok para que lo haga y esto actualiza los imports'''

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from utils.jwt_manager import create_token
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router

app = FastAPI(
    title= 'Aprendiendo FastApi',
    description= 'Una API para guardar peliculas db',
    version= '0.0.3',
    )

app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)

#In a very simplistic way create the database tables:
Base.metadata.create_all(bind=engine)


movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Accion'    
    }
]

@app.get('/', tags=['home'])
def myPage():
    return HTMLResponse ('<h1>Vamos negro</h1>')