"""
Pequeñas funciones anónimas pueden ser creadas con la palabra reservada lambda.
Las funciones Lambda pueden ser usadas en cualquier lugar donde sea requerido 
un objeto de tipo función. Están sintácticamente restringidas a una sola expresión.
"""

fac = lambda n: 1 if n <=1 else n*fac(n-1)
sumar = lambda a, b: a + b
doble = lambda n: n*2
par = lambda n: n%2 == 0
impar = lambda n: n%2 != 0
revertir = lambda cadena: cadena[::-1]

print(sumar(5,8))
print(doble(10))
print(par(6))
print(impar(13))
print(revertir('Hola Mundo'))
print(fac(5))

