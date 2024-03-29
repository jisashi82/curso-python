from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.client import db_client
from db.schemas.user import user_schema, users_schema
from bson import ObjectId

router = APIRouter(prefix='/userbd', tags=['userbd'], responses={
                   status.HTTP_404_NOT_FOUND: {'message': 'No Encontrado'}})

users_list = []


@router.get('/', response_model=list[User])
async def users():
    return users_schema(db_client.users.find())

@router.get('/{id}')
async def user(id: str):
    # llamar el path: http://localhost:8000/user/2
    return search_user("_id",ObjectId(id))


@router.get('/')
async def user(id: str):
    # llamar el path: http://localhost:8000/usersquery?id=2
   return search_user("_id",ObjectId(id))


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {'error': 'No se ha encontrado el usuario'}


@router.post('/', response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user: User):
    if type(search_user("email", user.email)) == User:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail="El usuario ya existe")

    #Convertimos a diccionario y eliminamos el id ya qye Mongo lo gestiona
    user_dict = dict(user)
    del user_dict['id']

    #insertamos el user_dict en Mongo y recuperamos el id que genera
    id = db_client.users.insert_one(user_dict).inserted_id


    new_user = user_schema(db_client.users.find_one({'_id': id}))
    return User(**new_user)


@router.put('/',response_model=User, status_code=status.HTTP_200_OK)
async def user(user: User):
    user_dict= dict(user)
    del user_dict["id"]
    try:
        db_client.users.find_one_and_replace({"_id":ObjectId(user.id)}, user_dict)
        
    except:
        return {'error': 'No se ha actualizado el usuario o no existe'}
    
    return search_user("_id", ObjectId(user.id))


@router.delete('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def delete(id: str):
    found = db_client.users.find_one_and_delete({"_id":ObjectId(id)})

    if not found:
        return {"error": "No se ha eliminado el usuario o no existe"}
    else:
        return {"message": "Se ha eliminado el usuario exitosamente"}


def search_user(key:str, value):
    try:
        user_tmp=user_schema( db_client.users.find_one({key:value}))
        return User(**user_tmp)
    except:
        return {'error':'No se ha encontrado el usuario'}