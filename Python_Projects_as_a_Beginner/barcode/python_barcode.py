"""
    Proyecto para generar codigos de barra con python-barcode.
    El programa solicita la cantidad de codigos que va a generar, luego solicita cada numero de codigo
    y el nombre del archivo, lo guarda en imagen SVG utilizando la clase 'ImageWriter'
"""

#first install pip install python-barcode
from barcode import EAN13, generate
from barcode.writer import ImageWriter
from io import BytesIO

num_barcodes= int(input("How Many Barcodes you Need?: "))
numbers= range(num_barcodes)
for i in numbers:
    id= input("Give 12-Digit number for you barcode id: ")
    my_code= EAN13(id, writer=ImageWriter)
    name =input("Give the name to save barcodes: ")
    my_code.save(name)
    

