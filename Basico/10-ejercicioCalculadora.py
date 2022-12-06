def menu():
    print("1.Sumar")
    print("2.Restar")
    print("3.Multiplicar")
    print("4.Dividir")
    print("0.Salir")
    opcion = int(input("Elige una opcion:: "))
    return opcion


def solicitaDatos():
    num1 = int(input("Indica el 1er. Numero: "))
    num2 = int(input("Indica el 2o. Numero: "))
    if num2 == 0:
        print("El numero no puede ser 0 \n")
        num2 = int(input("Indica el 2o. Numero: "))
    return num1, num2


def operacion(operador, num1, num2):
    if operador == "suma":
        resultado = num1 + num2
    elif operador == "resta":
        resultado = num1 - num2
    elif operador == "multiplica":
        resultado = num1 * num2
    elif operador == "divide":
        resultado = num1 / num2
    return resultado

while True:
    opcion= menu()
    #num1,num2 = solicitaDatos()
    
    if opcion==1:
        num1,num2 = solicitaDatos()
        print(f"el resultado de {num1} + {num2} = {operacion('suma',num1,num2)}")
    elif opcion==2:
        num1,num2 = solicitaDatos()
        print(f"el resultado de {num1} - {num2} = {operacion('resta',num1,num2)}")
    elif opcion==3:
        num1,num2 = solicitaDatos()
        print(f"el resultado de {num1} * {num2} = {operacion('multiplica',num1,num2)}")
    elif opcion==4:
        num1,num2 = solicitaDatos()
        print(f"el resultado de {num1} / {num2} = {operacion('divide',num1,num2)}")
    elif opcion == 0:
        print("Saliendo del programa...")
        break
    else:
        print("Elije una opcion valida\n")

    print("\n\n")