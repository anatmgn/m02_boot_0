#Recursividad: función cuenta atrás

def retrocontador(e):
    print("{},".format(e),end="")
    
    if e>0:
        retrocontador(e-1)
          
retrocontador(10)

def sumatorio(n):
    if n!=0:
        return n+sumatorio(n-1)
    else:
        return 0
sumatorio(4)


#no funciona factorial
def factorial(x):
    print("{},".format(x),end="")
    if x!=0:
        return x*factorial(x-1)
    else:
        return 0
          
          
          