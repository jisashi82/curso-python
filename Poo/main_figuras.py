from Figuras import Rectangulo,Circulo,calcularArea

def menu_principal():
    while True:
        menu="""
        --------------------------------------
        1.-Calcular el Area del Rectangulo
        2.-Calcular el Area del Circulo
        3.-Salir
        --------------------------------------
        INGRESE UNA OPCION: """
        opcion=input(menu.lstrip())
        match opcion:
            case '1':
                b= float(input('      Ingrese la base: '))
                a= float(input('      Ingrese la Altura: '))
                rectangulo=Rectangulo('Rectangulo',b,a)
                calcularArea(rectangulo)
            case '2':
                r= float(input('       Ingrese el radio: '))
                circulo=Circulo('Circulo',r)    
                calcularArea(circulo)
            case '3':
                print('Saliendo de la App')
                break

def main():
    menu_principal()
    

if __name__=='__main__':
    main()