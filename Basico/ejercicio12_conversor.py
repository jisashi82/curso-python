def conversion(valor_dolar, pais):
    cantidad_moneda = float(input(f"ingrese la cantidad de {pais}: "))

    dolares = round(cantidad_moneda / valor_dolar, 2)
    print(f'Tienes ${dolares} Dolares')

def menu():
    salir=False
    while(salir==False):
        print('==' * 25)
        layout="""
        1.-Convertir Peso Mexicano a Dolar
        2.-Convertir Soles Peruano a Dolar
        3.-Convertir Peso Argentino a Dolar
        4.-Salir
        Seleccione una opcion:  """
        
        print('==' * 25)
        opcion=input(layout)
        
        match opcion:
            case '1':
                conversion(18.77,'Pesos Mexicanos')
            case '2':
                conversion(3.61, 'Soles Peruanos')
            case '3':
                conversion(23.12,'Pesos Argeninos')
            case '4':
                salir=True
            case _:
                print('Seleccione una opcion valida')
                
        print('\n'*2)
        
        
def main():
    menu()

if __name__=='__main__':
    main()