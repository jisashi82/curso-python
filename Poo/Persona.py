
class Persona:
    #esto podria comentarse ya que esta definido en el constructor
    #nombre = None
    #edad = None
    
    #constructor: cuando se define ya no es necesario declarar los atributos en la parte superior
    def __init__(self,nombre,edad) -> any:
        self.__nombre=nombre
        self.__edad=edad
    
    #metodo para mostrar los datos
    def mostrar_datos(self):
        print(f'Nombre: {self.__nombre} \nEdad: {self.__edad}')
    
    #similar al metodo toString, sin este metodo se imprime la referencia de memoria    
    def __str__(self) -> str:
        return f'Nombre:{self.__nombre} Edad:{self.__edad}'
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self,nombre):
        self.__nombre=nombre
        
    def getEdad(self):
        return self.__edad
    
    def setNombre(self,edad):
        self.__nombre=edad

#Esta clase hereda de la clase Persona utilizando metodos super()        
class Empleado(Persona):
    
    def __init__(self, nombre, edad,sueldo) -> any:
        super().__init__(nombre, edad)
        self.__sueldo=sueldo
    
    def detalle_empleado(self):
        super().mostrar_datos()
        print(f'sueldo: {self.__sueldo}')
    
    def __str__(self) -> str:
        return super().__str__() +f' Sueldo: {self.__sueldo}'