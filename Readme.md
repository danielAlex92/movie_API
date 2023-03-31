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
3. Hago mi enlace con el repositorio remoto al que quiero subir el proyecto
```sh
git remote add origin https://github.com/danielAlex92/movie_API.git
```
4. Agrego todos los archivos del proyecto al area de stage
```sh
git add .
```
5. Hago commit para enviar mis archivos al repositorio local
```sh
git commit -m "Deploy1"
```
6. Hago push para enviar mi repositorio local al repo remoto
```sh
git push -u origin main
```
- Obtengo la respuesta:
```
Updates were rejected because the remote contains work that you do
not have locally. This is usually caused by another repository pushing
to the same ref. You may want to first integrate the remote changes
(e.g., 'git pull ...') before pushing again.
See the 'Note about fast-forwards' in 'git push --help' for details.
```
- Este error se debe a que lo que está en el repositorio remoto es diferente a lo del local, así que debo integrarlos. Se recomienta hacer un git pull que traiga el repo remoto hacia el local
- Verifico que el repo remoto sea 'origin' y que me muestre su URL, con:
```sh
git remote
git remote -v
```
- (origin es simplemente el nombre predeterminado que recibe el repositorio remoto principal contra el que trabajamos.)

7. Hago git pull intentando traer lo del repo remoto, en este caso hay error porque los commits del repo local son diferentes a los del repo remoto:
```sh
git pull origin main 
(fatal: refusing to merge unrelated histories)
```
8. Agrego una instruccion adicional a git para permitir historias no relacionadas:
```sh
git pull origin main --allow-unrelated-histories
From https://github.com/danielAlex92/movie_API
 * branch            main       -> FETCH_HEAD
Merge made by the 'ort' strategy.
```
9. Finalmente puedo hacer el push con exito:
```sh
git push origin main
```

## Hosting: Railway

1. Creo cuenta en la pagina de Railway y la vinculo con el repo en Github del proyecto
2. Al dar deploy a la app dan multiples errores, por lo cual hacemos las siguientes modificaciones en el archivo main.py para que la aplicación corra automaticamente en el servidor remoto de Railway:
```py
import uvicorn, os

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0",
                port=int(os.environ.get("PORT", 8000)))
```
3. Ademas hacemos la siguiente modificacion en el archivo error_handler ya que la sintaxis anterior no es aceptada por python 3.8 que es la version que maneja Railway
```py
Response| JSONResponse
por:

from typing import Union
Union[Response, JSONResponse]:
```
4. Railway dice que el proyecto es montado con exito y por ultimo vamos a settings y le damos en crear dominio, nos genera el siguiente y ahi podemos ver nuestra app ya desplegada:

https://movieapi-production-0354.up.railway.app/