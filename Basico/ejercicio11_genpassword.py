import random

def generarPassword():
    mayusculas=['A','B','C','D','E','F','G']
    minusculas=['a','b','c','d','e','f','g']
    simbolos=['!','@','#','$','&','%']
    
    #genera una lista del 0 al 9 mediante comprension de listas
    numeros=[str(x) for x in range(0,10)]
    
    caracteres= mayusculas+minusculas+simbolos+numeros
    contrasena=[]
    
    for i in range(0,15):
        contrasena.append(random.choice(caracteres))
    
    contrasena="".join(contrasena)
    
    return contrasena

def main():
    password= generarPassword();
    print(f'Tu contraseña es: {password}')
    

if __name__=='__main__':
    main()