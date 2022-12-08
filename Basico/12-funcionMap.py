"""/*las funciones anonimas se declaran en una sola linea a usando el prefijo 'lambda'"""
#funcion map
lista = [23,54,56,23,78,23,66,72]
print(list(map(lambda valor: valor*valor,lista)))

#funcion filter.- filtrar los numero pares
print(list(filter(lambda valor: valor%2==0, lista)))

#funcion reduce.-suma todos los valores de la lista
import functools
print(str(functools.reduce(lambda x,resultado:x+resultado, lista)))