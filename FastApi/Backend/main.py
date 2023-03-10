from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import products, users, basic_auth_users, jwt_auth_users,users_db

app=FastAPI()

#Routers
app.include_router(products.router)
app.include_router(users.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)

#Montando la carpeta static
app.mount(path='/static', app= StaticFiles(directory='static'), name='static')

@app.get("/")
async def root():
    return {"message": '¡Hola FastApi!'}


#Inicia el server: uvicorn main:app --reload
#Documentacion con Swagger: http://127.0.0.1:8000/docs
#Documentacion con Redocly: http://127.0.0.1:8000/redoc