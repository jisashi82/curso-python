import random

def jugar(intentos):
    numero_elegido=None
    numero_aleatorio= random.randint(1,100)
    
    while(numero_elegido != numero_aleatorio):
        numero_elegido=int(input('Ingrese un numero: '))
         
        if(numero_elegido > numero_aleatorio):
             print('elige un numero mas pequeño')
             intentos-=1
        elif(numero_elegido<numero_aleatorio):
            print('Elige un numero mas grande')
            intentos-=1
        
        if(intentos == 0):
            print('GAME OVER')
            print(f'El numero era: {numero_aleatorio}')
            break
        
        print(f'Te quedan {intentos} intentos')
        
    if numero_elegido == numero_aleatorio:
        print('Felicidades Ganaste!')
    
def main():
    menu="""
    1.- Modo Facil(10 intentos)
    2.- Modo Dificil(5 intentos)
    3.- Salir
    INGRESE UNA OPCION: 
    """
    
    while True:
        opcion=input(menu)
        match opcion:
            case '1':
                jugar(10)
            case '2':
                jugar(5)
            case '3':
                break
        

if __name__=='__main__':
    main()