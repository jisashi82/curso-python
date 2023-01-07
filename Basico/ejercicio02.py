#Aplicacion 02: detectar si un caracter ingresado es vocal

letra = input('Ingresa un caracter: ')
letra =letra.lower()
if(letra == 'a' or letra =='e' or letra=='i' or letra=='o' or letra=='u'):
    print(f'El caracter {letra} es una vocal')
else:
    print(f'El caracter {letra} no es vocal')