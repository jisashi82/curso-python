from os import path
from io import open

def escribir_archivo():
    file = open('texto.txt', 'w')
    file.write('Hola Mundo de Python')
    file.close()

def leer_archivo():
    if path.isfile('texto.txt'):
        #abre el archivo en modo lectura(read)
        file = open('texto.txt', 'r')
        textos = file.read()
        file.close()
        print(textos)
    else:
        print('No existe el archivo')

def agregar_datos():
    if path.isfile('texto.txt'):
        #abre el archivo en modo appending para escribir al final del archivo
        file = open('texto.txt', 'a')
        file.write('\nHola Jisashi')
        file.close()
    else:
        print('No existe el archivo')

def modificar_datos():
    if path.isfile('texto.txt'):
        #abre el archivo en modo lectura y el + es para update(modificar)
        file = open('texto.txt', 'r+')
        #obtenemos el contenido del archivo como una lista
        textos = file.readlines()
        #imprime la lista
        print(textos)
        #mofifica el elemento de acuerdo al indice
        textos[1]='Hola Jordan poole\n'
        #imprime los cambios
        print(textos)
        #seek para posicionar el puntero al primer caracter
        file.seek(0)
        #writelines escribe la lista al archivo
        file.writelines(textos)
        #se cierra el archivo
        file.close()
    else:
        print('No existe el archivo')
        
def eliminar_datos():
    file = open('texto.txt', 'w')
    file.close()
            
        
        
#escribir_archivo()
agregar_datos()
leer_archivo()
modificar_datos()