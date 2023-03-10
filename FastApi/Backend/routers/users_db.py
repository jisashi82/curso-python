from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.client import db_client
from db.schemas.user import user_schema, users_schema

router = APIRouter(prefix='/userbd', tags=['userbd'], responses={
                   status.HTTP_404_NOT_FOUND: {'message': 'No Encontrado'}})

users_list = []


@router.get('/', response_model=list[User])
async def users():
    return users_schema(db_client.local.users.find())

@router.get('/{id}')
async def user(id: int):
    # llamar el path: http://localhost:8000/user/2
    return search_user(id)


@router.get('/')
async def user(id: int):
    # llamar el path: http://localhost:8000/usersquery?id=2
    return search_user(id)


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {'error': 'No se ha encontrado el usuario'}


@router.post('/', response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user: User):
    if type(search_user_by_email(user.email)) == User:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail="El usuario ya existe")

    #Convertimos a diccionario y eliminamos el id ya qye Mongo lo gestiona
    user_dict = dict(user)
    del user_dict['id']

    #insertamos el user_dict en Mongo y recuperamos el id que genera
    id = db_client.local.users.insert_one(user_dict).inserted_id


    new_user = user_schema(db_client.local.users.find_one({'_id': id}))
    return User(**new_user)


@router.put('/')
async def user(user: User):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
            break

    if not found:
        return {'error': 'No se ha actualizado el usuario o no existe'}
    else:
        return {'message': 'Se ha actualizado el usuario exitosamente'}


@router.delete('/{id}')
async def user(id: int):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
            break

    if not found:
        return {'error': 'No se ha eliminado el usuario o no existe'}
    else:
        return {'message': 'Se ha eliminado el usuario exitosamente'}


def search_user_by_email(email:str):
    try:
        user_tmp=user_schema( db_client.local.users.find_one({'email':email}))
        return User(**user_tmp)
    except:
        return {'error':'No se ha encontrado el usuario'}