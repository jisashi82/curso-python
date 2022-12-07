def calcular(num1,num2, operacion='sumar'):
    def sumar(num1,num2):
        return num1+num2
    def restar(num1,num2):
        return num1-num2
    def multiplicar(num1,num2):
        return num1*num2
    def dividir(num1,num2):
        return num1/num2
    
    if(operacion=='sumar'):
        print(f"{num1} + {num2} = {sumar(num1,num2)}")
    elif(operacion=='restar'):
        print(f"{num1} - {num2} = {restar(num1,num2)}")
    elif(operacion=='multiplicar'):
        print(f"{num1} * {num2} = {multiplicar(num1,num2)}")
    elif(operacion=='dividir'):
        print(f"{num1} / {num2} = {dividir(num1,num2)}")

calcular(5,3)
calcular(5,8,"multiplicar")
calcular(9,3,"dividir")
calcular(100,88,"restar")