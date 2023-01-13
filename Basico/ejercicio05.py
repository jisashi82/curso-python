#Entrada de datos del consumo
consumo=float(input('Introduce el monto del consumo: '))
descuento =0.0
impuesto=0.0

if(consumo>=0):
    
    if(consumo <= 100):
        dato_desc='10%'
        descuento = consumo *0.10
    elif(consumo>100 and consumo <= 200):
        dato_desc='20%'
        descuento = consumo *0.20
    else:
        dato_desc='30%'
        descuento = consumo *0.30
    
    monto = consumo -descuento
    impuesto =monto *0.19

    total_pagar= monto + impuesto

    #Salida de datos
    print('=='*30)
    print('Factura de Consumo')
    print(f'Descuento que se aplica: {dato_desc}')
    print('=='*30)
    print(f'Consumo: {consumo}')
    print('Monto del Descuento: ',round(descuento,2))
    print('Impuesto: ',round(impuesto,2))
    print('Total a pagar: ',round(total_pagar))
else:
    print('Error al ingresar el monto del consumo')
    
