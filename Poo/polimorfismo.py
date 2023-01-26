

class Persona():
    def __init__(self,nombre) -> None:
        self.__noombre= nombre
    
    def moverse(self):
        print('Ando caminando')

#Se sobrescribe el metodo moverse en cada clase heredada de Persona para simular el polimorfismo
class Atleta(Persona):
    def moverse(self):
        return print('Ando corriendo')

class Ciclista(Persona):
    def moverse(self):
        return print('Ando en Bici')