from fastapi import Depends, APIRouter, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter(prefix='/basicauth', tags=['basicauth'], responses={
                   status.HTTP_404_NOT_FOUND: {'message': 'No Encontrado'}})


oauth2 = OAuth2PasswordBearer(tokenUrl='login')

class User(BaseModel):
    username:str
    fullname:str
    email:str
    disabled:bool
    
class UserDB(User):
    password:str
    

users_db={
    'jisashi82':{
        'username':'jisashi82',
        'fullname':'Jisahi Nakamura',
        'email':'jisashi@gmail.com',
        'disabled':True,
        'password':'123456'
    },
     'abel27':{
        'username':'abel27',
        'fullname':'Abel Ramos',
        'email':'abel@gmail.com',
        'disabled':False,
        'password':'654321'
    }
}

def search_user(username:str):
    if username in users_db:
        return UserDB(**users_db[username])
    
def search_user_db(username:str):
    if username in users_db:
        return User(**users_db[username])
    
async def current_user(token:str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Credenciales Invalidas',headers={'WWW-Authenticate':'Bearer'})
    
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Usuario Inactivo')
    
    return user
    

@router.post('/login')
async def login(form:OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    user = search_user_db(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Usuario no es correcto')
    
    if not form.password == user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='La contraseña no es correcta')
    
    return {'access_token':user.username, 'token_type':'bearer'}


@router.get('/users/me')
async def me(user:User = Depends(current_user)):
    return user