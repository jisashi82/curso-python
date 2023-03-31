import string

numbers=list()

with open("numbers.csv", "r") as archivo:
    contenido=archivo.read()
    
    tmpStr=''
    for eachLine in contenido:
           
        if eachLine.isdigit():
            tmpStr+=eachLine
        elif eachLine==',' and tmpStr !='':
            numbers.append(int(tmpStr))
            tmpStr=''
    if tmpStr.isdigit():
            numbers.append(int(tmpStr))

    print(numbers)     
   
   
"""El código dado realiza la lectura de un archivo `numbers.txt` 
   que contiene números separados por comas y los almacena en una lista llamada `numbers`. 
   Sin embargo, existen algunas mejoras que se pueden hacer para hacer que el código sea más legible y eficiente. 
   En particular, se puede reemplazar el ciclo `for eachLine in contenido` 
   por una expresión generadora `contenido.split(',')` que divide el contenido en el archivo según los caracteres ',':
   
   input file numbers.csv:
   1,2,pete,
    3,
    4,dan,5,
    6,7,8,richard,10,11,12,13,
    p,16,evan,14,
    15

"""   
#Refactoring with chatGPT  no funciono excluye algunos numeros   
# with open("numbers.csv", "r") as archivo:
#     contenido = archivo.read()
#     print(contenido.split(','))
#     numbers = [int(x) for x in contenido.split(',') if x.isdigit()]
#     print(numbers)
 