from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import products, users

app=FastAPI()

#Routers
app.include_router(products.router)
app.include_router(users.router)
app.mount(path='/static', app= StaticFiles(directory='static'), name='static')

@app.get("/")
async def root():
    return {"message": '¡Hola FastApi!'}


#Inicia el server: uvicorn main:app --reload
#Documentacion con Swagger: http://127.0.0.1:8000/docs
#Documentacion con Redocly: http://127.0.0.1:8000/redoc