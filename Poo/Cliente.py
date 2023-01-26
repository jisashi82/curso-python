from Persona import Persona

class Cliente(Persona):
    
    def __init__(self, nombre, edad, telefono) -> any:
        #super().__init__(nombre, edad)
        Persona.__init__(self,nombre,edad)
        self.__telefono=telefono
        
    def detalle_cliente(self):
        #super().mostrar_datos()
        Persona.mostrar_datos(self)
        print(f'Telefono: {self.__telefono}')
        
    def __str__(self) -> str:
        #return super().__str__() +f' Telefono:{self.__telefono}'
        return Persona.__str__(self) + f' Telefono:{self.__telefono}'