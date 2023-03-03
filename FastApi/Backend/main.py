from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def root():
    return {"message": '¡Hola FastApi!'}


#Inicia el server: uvicorn main:app --reload
#Documentacion con Swagger: http://127.0.0.1:8000/docs
#Documentacion con Redocly: http://127.0.0.1:8000/redoc