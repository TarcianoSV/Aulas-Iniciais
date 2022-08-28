import math
def fatorial(numero):
    resultado=numero
    while numero>0:
        if numero!=1:
            resultado=resultado*(numero-1)
        numero=numero-1
    return resultado

print(fatorial(6))

resultado=math.factorial(6)
print(resultado)
