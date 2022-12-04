#Generadores

def impares():
    for num in range(1,50,2):
        yield num
        
generador = impares()
print(generador)


print(next(generador))
print(next(generador))
print(next(generador))

print("\n --ciclo for--\n")
for i in generador:
    print(i)

