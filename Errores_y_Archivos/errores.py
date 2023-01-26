c=0
suma=0
while c<3:
    try:
        n=int(input('Ingrese un numero: '))
        suma+=n
        c+=1
    except:
        print('Error: Ingrese solo numeros enteros ')
    else:
        print('Todo funciono correctamente')
    finally:
        print('Fin de la ejecucion')

print(suma)