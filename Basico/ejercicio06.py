import random

pares=[]
impares=[]
numeros=tuple(map(lambda x: x, range(1,10)))
print(numeros)


for n in numeros:
    numero_random= random.randint(1,100)
    resultado=n*numero_random
    
    if resultado % 2 ==0:
        print(f'{n} x {numero_random} = {resultado}')
        pares.append(resultado)
    else:
        print(f'{n} x {numero_random} = {resultado}')
        impares.append(resultado)
        
        
print('Lista de Pares: ', pares)
print('Lista de Pares: ', impares)