class OperadorException(Exception):

    def __init__(self,mensaje):
        super().__init__(mensaje)

def dividir(a,b):
    if b==0:
        #raise ZeroDivisionError('No se puede dividir entre cero!')
        raise OperadorException('No se puede dividir entre cero!')
    else:
        return a/b

print(dividir(4,0))