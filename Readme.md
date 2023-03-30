# Curso Python framework FastAPI Base de Datos, Modularización y Deploy a Producción

Vamos a trabajar con un ORM de FastAPI llamado sqlalchemy para crear bases de datos
y hacer CRUD

## SQLAlchemy 
Es una biblioteca de Python para trabajar con bases de datos relacionales. Ofrece una manera de interactuar con las bases de datos a través de un modelo de objetos, sin tener que escribir manualmente sentencias SQL.

## SQLModel
Otra opcion de ORM creada por el mismo creador de FastAPI (tiangolo)

- Generar el archivo requirements con el siguiente comando
```sh
pip freeze > requirements.txt
```
- Instalar las dependencias necesarias para contribuir más rápido en proyectos
```sh
pip install -r requirements.txt
```
- Por consola, entrar en la carpeta del proyecto , y crear el ambiente virtual, se creará la carpeta env
```sh
python -m venv venv
```
- Activar el ambiente, al hacerlo, en la ruta de la terminal aparece (env) como marca de que estamos dentro del entorno virtual
```
En Windows con bash, ejecuta:
source venv/Scripts/activate
```
- Creamos script en Python importando FastAPI y para ejecutarlo, corremos la app en un server así:
```sh
uvicorn main:app --reload
```

1. Instalamos la extension para VSCode llamada SQLite viewer

2. Luego, dentro de nuestro entorno virtual instalamos sqlalchemy

```sh
pip install sqlalchemy
```
3. En la carpeta de nuestro proyecto creamos una carpeta llamada config, dentro le colocamos un archivo llamado __init__.py para que reconozca la carpeta como un modulo.

4. También en esta carpeta creamos un archivo llamado database.py donde creamos el motor y la sesion de nuestra DB

5. Creamos una carpeta llamada models, tambien con un archivo __init__ donde creamos el archivo movie.py en el cual creamos el modelo de nuestra tabla.

6. Ejecutamos la aplicación y nuestra tabla se crea en la raiz, podemos ver su interior gracias a la extension SQLite
```sh
uvicorn 01_createDBTable:app --reload
```
## Middleware
- El middleware es un software con el que las diferentes aplicaciones se comunican entre sí. Brinda funcionalidad para conectar las aplicaciones de manera inteligente y eficiente, de forma que se pueda innovar más rápido. El middleware actúa como un puente entre tecnologías, herramientas y bases de datos diversas para que pueda integrarlas sin dificultad en un único sistema. Sin la ayuda del middleware, los desarrolladores tendrían que crear un módulo de intercambio de datos para cada componente de software que se conecta con la aplicación. Esto representa un desafío muy grande, ya que las aplicaciones modernas consisten en múltiples microservicios o componentes de software pequeños que interactúan.

1. En este proyecto usamos un middleware para manejo de errores.
2. Creamos una carpeta en la raiz del proyecto llamada middlewares, agregamos un archivo __init__ para que lo reconozca como un modulo y agregamos un archivo error_handler donde está la logica para manejar nuestros erroress

## Routers
- Dividimos nuestro proyecto en modulos, creamos carpeta routers y llevamos allá los metodos HTTP
- Enlazamos los router a traves de la clase APIRouter()

# Deploy

- Nos aseguramos de hacer un gitignore y el archivo requirements.txt

1. Creo Repo en Github o Gitlab
2. Creo repositorio local en mi carpeta local del proyecto
```sh
git init --initial-branch=main
```

git remote add origin https://github.com/danielAlex92/movie_API.git

git add .

git commit -m "Deploy1"

git push -u origin main