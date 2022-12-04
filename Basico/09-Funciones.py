#se define la funcion con la palabra reservada def
def esPar(numero):
    if(numero %2 == 0):
        print("El numero es par")
    else:
        print("El numero es impar")
        

#funcion que suma 2 numeros
def suma(num1,num2):
    return num1 + num2

#implementado la funcion esPar
numero= int(input("Indica un numero para ver si es par: "))
esPar(numero)
esPar(21)
esPar(28)

#implementado la funcion suma
num1=int(input("numero1: "))
num2=int(input("numero2: "))
#resultado= suma(num1,num2)
print(f"Suma {suma(num1,num2)}")