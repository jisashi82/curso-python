# Aplicación 01: Crear un sistema que detecte si número es par positivos o
# par negativo y también si es impar positivo o negativos y si el numero ingresado es 0 que detecte si es neutro.

num = int(input('Ingresa un numero entero: '))

if(num == 0):
    print(f'El numero  {num} es neutro')
elif (num > 0 and num%2 == 0):
    print(f'El numero {num} es par positivo')
elif(num < 0 and num%2==0):
    print(f'El numero {num} es par negativo')
elif(num < 0 and num%2!=0):
    print(f'El numero {num} es impar negativo')
else:
    print(f'El numero {num} es impar positivo')