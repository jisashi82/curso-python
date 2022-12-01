#Variables en python

myVariable="   Esto es una variable de string   "
print(type(myVariable))
print(myVariable)

my_int_variable=5
print(type(my_int_variable))
print(my_int_variable)

my_bool_variable=False
print(type(my_bool_variable))
print(my_bool_variable)

my_float_variable=12.34
print(type(my_float_variable))
print(my_float_variable)

#Ejemplo con las cadenas-------------------------------------------------------
print(len(myVariable))
print(myVariable.__len__())
#cambia a minnuscula la cadena
print(myVariable.lower())
#cambia a mayusculas
print(myVariable.upper())
#imprime la primer letra en Mayuscula de una cadena
print(myVariable.capitalize())
#imprimir una porcion de la cadena
print(myVariable[2:7])
#eliminar espacios al inicio y final de una cadena
print(myVariable.strip())
#reemplazar parte de una cadena de texto
print(myVariable.replace("string","integer"))
#concatenacion automatica
print('cadena 1'' cadena2')