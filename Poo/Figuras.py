from math import pi


class Figura():
    def __init__(self, nombre):
        self.__nombre = nombre

    def area(self):
        pass

    def perimetro(self):
        pass

    def getNombre(self):
        return self.__nombre


class Rectangulo(Figura):
    def __init__(self, nombre, base, altura):
        super().__init__(nombre)
        self.__base = base
        self.__altura = altura

    def area(self):
        return self.__base * self.__altura

    def perimetro(self):
        return 2*self.__base + 2*self.__altura


class Circulo(Figura):
    def __init__(self, nombre, radio):
        super().__init__(nombre)
        self.__radio = radio

    def area(self):
        return pi * (self.__radio**2)

    def perimetro(self):
        return 2*pi * self.__radio

# usando polimorfismo


def calcularArea(figura: Figura):
    print(f'El area del {figura.getNombre()} es {figura.area()}')
    print(f'El perimetro del {figura.getNombre()} es {figura.perimetro()}')
