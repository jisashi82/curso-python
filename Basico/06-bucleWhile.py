# Ejemplo de tabla de multiplicar

#solicita el numero para calcular la tabla de multiplicar
tabla = int(input("Indica el numero de tabla quieres calcular: "))
print(f"\n Tabla del numero {tabla}")

contador = 1
while contador < 11:
    #calculamos la tabla de multiplicar
    resultado = tabla * contador
    #mostramos el resultado
    print(f"{tabla} x {contador} = {resultado}")
    #incrementamos el numero secuencial de la variable contador 
    contador = contador + 1

print("Fin de la tabla de multiplicar")