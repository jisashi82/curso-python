#tabla de multiplicar con for

tabla=int(input("Indica el numero de la tabla a multiplicar: "))
print(f"Tabla del {tabla}")

#repetir minetra sea menor que 11
for contador in range(1,11):
    resultado = tabla * contador
    print(f"{tabla} x {contador} = {resultado}")
    
print("Fin de la tabla")


#Ejemplo de For copn listas
nombres=["Abel", "Jisashi", "Miguel", "Cristian"]
for nombre in nombres:
    print(f"Hola {nombre}")
    
#Ejemplo Imprime los numeros del 1 al 100
for num in range(100):
    print(num +1)
    
#Ejemplo de For-Else
print(f"\n Ejemplo de For-Else -------")
mi_color="Naranja"
colores=["Azul", "Blanco", "Verde", "Amarillo", "Rojo"]
for color in colores:
    print(color)
    if(color == mi_color):
        print("color encontrado")
        break
else:
    print(f" No se encontro el color {mi_color}")