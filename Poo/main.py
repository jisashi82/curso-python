from Persona import Persona,Empleado
from Cliente import Cliente

persona1= Persona('Jisashi', 39)
#persona1.nombre='Jisashi'
#persona1.edad=39

persona2 =Persona('Abel',40)
persona2.setNombre('Abel2')
#persona2.edad =40

persona2.mostrar_datos()
print('=='*15)

#imprime los datos utilizando el metodo __str__ definido en la clase Persona
print(persona1)

print('\n===Empleado===')
empleado1=Empleado('Maria',25,1200)
empleado1.detalle_empleado()
print(empleado1)

print('\n===Cliente===')
cliente1= Cliente('Raul',33,'962-144-6789')
print(cliente1)