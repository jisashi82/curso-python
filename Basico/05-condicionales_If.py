numero1=int(input("Dime el 1er. numero: "))
numero2=int(input("Dime el 2o. numero: "))

if(numero1>numero2):
    print("el numero mayor es ",numero1)
elif(numero1 < numero2):
    print(f"el numero {numero1} es menor que el numero {numero2} ")
else:
    print("Son iguales")
    
    
#Segundo Ejemplo----------------------------------------------------------
edad = int(input("\nDime tu edada y te indico el precio: "))
if(edad < 5):
    precio = 0
elif edad <=15:
    precio = 5
elif edad <= 40:
    precio=10
elif edad <=59:
    precio=15
else:
    precio=20
    
print("El precio de acuerdo a tu edad es:"+ str(precio))