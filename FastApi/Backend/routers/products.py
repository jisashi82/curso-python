from fastapi import APIRouter

router= APIRouter(prefix='/products', responses={404:{'message':'No Encontrado'}})

products_list = ['Producto 1','Producto 2','Producto 3','Producto 4', 'Producto 5']

@router.get('/')
async def home():
    return products_list


@router.get('/{id}')
async def home(id:int):
    return products_list[id]

