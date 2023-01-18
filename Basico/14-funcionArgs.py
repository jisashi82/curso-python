# Define una funcion con argumentos indeterminados
# *args se utiliza para argumentos indeterminados por posicion
# **kargs se utiliza para argumentos por nombres


def sumar(*args, **kargs):
    suma = 0
    for n in args:
        suma += n
    # en python se pueden retornar mas de 1 valor
    return suma, kargs


suma_total, datos = sumar(1, 2, 3, 4, 5, 6, 7, nombre="Jisashi", edad=40)
print(f"La suma total es: {suma_total}")
print(f"argumentos por nomnbre: {datos}")
