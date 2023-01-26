division=0
try:
    a=int(input('Ingrese el Dividendo: '))
    b=int(input('Ingrese el Divisor: '))
    
    division=a/b
except ZeroDivisionError:
    print('Error: no se puede dividir entre cero!')
except ValueError:
    print('Ingrese un numero entero')
except Exception as error:
    print('Ha ocurrido un error no previsto: ',type(error).__name__)