from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse

# Esta clase hereda de BaseHTTPMiddleware, super() hace referencia a esta última
class ErrorHandler(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI) -> None: # Le pasamos el tipo de nuestra app en este caso FastAPI
        super().__init__(app)

# Metodo que detecta si ocurre un error en nuestra aplicación
# call_next hace referencia a la siguiente llamada, si no hay errores se ejecuta
# Devuelve un Response en caso de que no ocurra un error y JsonResponse cuando hay error
    async def dispatch(self, request: Request, call_next) -> Response | JSONResponse:
        try:
            return await call_next(request)
        except Exception as e:
            return JSONResponse(status_code=500, content={'error': str(e)})