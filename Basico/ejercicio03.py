#ingresa un numero y suma los numero anteriores


num = int(input('Ingresa un numero entero: '))
resultado=0
while(num > 0):
    resultado+=num
    num-=1
    
print(f'La suma es: {resultado}')



#uso del break
print('=='*20)
i=0
while i < 10:
    i+=1
    print(i)
    
    if(i == 5):
        print('Termina el bucle')
        break
else:
    print('Termina el While')