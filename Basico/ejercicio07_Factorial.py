# Ejemplo de factorial de un numero.- solicita un numero y calcula el factorial

f=[1]
def factorial(n):
    #print('Valor inicial =>', n)
    if n>1:
        n= n* factorial(n-1)
        f.append(n)
    
    #print('Valor final =>', n)
    return n

num=int(input('Introduce un numero: '))
print(f'El factorial de {num}  es:',  factorial(num))
print(f)