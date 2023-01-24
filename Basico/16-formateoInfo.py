from sys import argv

if len(argv) == 4:
    nombre = argv[1]
    edad=int(argv[2])
    altura=float(argv[3])
    
    #print(f'Nombre:{nombre} \nEdad:{edad} \nAltura:{altura}')   
    print('Nombre:{} \nEdad:{} \nAltura:{}'.format(nombre,edad,altura))
    print(f'Nombre:%s \nEdad:%i \nAltura: %f'%(nombre,edad,altura))   
else:
    print('Error, ingrese los argumentos correctos')
    print('Ej.: formateoInfo.py "Nombre" 5 1.87')    
