
def fibo(n):
    a,b= 0,1
    while a< n:
        print(a, end=' ')
        a,b= b, a+b
    
    print()
    

def fibo2(n):
    lista=[]
    a,b= 0,1
    while a< n:
       lista.append(a)
       a,b= b, a+b
    return lista
    
    