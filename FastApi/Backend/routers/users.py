from fastapi import APIRouter,HTTPException
from pydantic import BaseModel

router= APIRouter()

#Inicia el server: uvicorn users:router --reload

#Entidad User
class User(BaseModel):
    id:int
    name:str
    surname:str
    telefono:str
    age:int
    
users_list=[User(id=1,name='Abel',surname='Ramos',telefono='96214413326',age=41),
            User(id=2,name='Jisashi',surname='Nakamura',telefono='9624445666',age=41),
            User(id=3,name='Said',surname='Ramos',telefono='9616789876',age=35)]

@router.get('/usersjson')
async def usersjson():
    return [
        {'name': 'Jisashi', 'surname':'nakamura','telefono':'9621334567', 'age':41},
        {'name': 'Abel', 'surname':'Ramos','telefono':'9611634968', 'age':20},
        ]
    
@router.get('/users')
async def users():
    return users_list

@router.get('/user/{id}')
async def user(id:int):
    #llamar el path: http://localhost:8000/user/2
    return search_user(id)
        

@router.get('/user/')
async def user(id:int):
    #llamar el path: http://localhost:8000/usersquery?id=2
    return search_user(id)
    

def search_user(id:int):
    users= filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {'error':'No se ha encontrado el usuario'}
    

@router.post('/user/',status_code=201)
async def user(user:User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=204, detail='El usuario ya existe')
        #return {'error': 'El usuario ya existe'}
    else:
        users_list.append(user)
        return {'message': 'Se ha insertado el usuario'}
    
@router.put('/user/')
async def user(user:User):
    found=False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id== user.id:
            users_list[index]= user
            found=True
            break
            
    if not found:
        return {'error':'No se ha actualizado el usuario o no existe'}
    else:
        return {'message':'Se ha actualizado el usuario exitosamente'}
    

@router.delete('/user/{id}')
async def user(id:int):
    found=False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id== id:
            del users_list[index]
            found=True
            break
            
    if not found:
        return {'error':'No se ha eliminado el usuario o no existe'}
    else:
        return {'message':'Se ha eliminado el usuario exitosamente'}