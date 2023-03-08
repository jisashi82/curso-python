from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from datetime import datetime,timedelta
import jwt


ALGORITHM='HS256'
ACCESS_TOKEN_DURATION= 15
SECRET ="363453af30a0b1093775d0be01f758bd174740543c74ee059a61326554395791"

app=FastAPI()


oauth2 = OAuth2PasswordBearer(tokenUrl='login')

crypt= CryptContext(schemes=['bcrypt'])

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
        'password':'$2a$12$b6wW7euggpePVS9qfQwYH.bAF.KhdVUeyJGBeMoz/NxRyC7kOZyJi'
    },
     'abel27':{
        'username':'abel27',
        'fullname':'Abel Ramos',
        'email':'abel@gmail.com',
        'disabled':False,
        'password':'$2a$12$2akzuzaUqAjXP1yr0Y9hZOALUxYvc9aeokLurcMbR0jDugTIC7Hj.'
    }
}

 
def search_user_db(username:str):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username:str):
    if username in users_db:
        return User(**users_db[username])
    
    
async def auth_user(token:str =Depends(oauth2)):
    exception= HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Credenciales Invalidas',headers={'WWW-Authenticate':'Bearer'})
    try:
        username = jwt.decode(token, SECRET, ALGORITHM).get('sub')
        if username == None:
            raise exception   
    except jwt.PyJWTError:
        raise exception
    
    return search_user(username)
            
    
async def current_user(user:User = Depends(auth_user)):
    if user.disabled == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Usuario Inactivo')
    
    return user


@app.post('/login')
async def login(form:OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    user = search_user_db(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Usuario no es correcto')
    
    if not crypt.verify(form.password,user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='La contraseña no es correcta')
    
    expire =datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_DURATION)        
    #payload={'sub':user.username, 'exp': expire}        
    payload={'sub':user.username, 'exp': expire}        
    token= jwt.encode(payload, SECRET, ALGORITHM)
    
    return {'access_token': token, 'token_type':'bearer'}


@app.get('/users/me')
async def me(user:User = Depends(current_user)):
    return user