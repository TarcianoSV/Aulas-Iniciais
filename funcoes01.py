from random import randint
from time import sleep

def numeroaleatorio():
    '''gera um numero aleatorio entre 1 e 200 '''
    return randint(1,200)

def aguardando():
    sleep(3)
    return 0

def soma(numero1, numero2):
    return int(numero1)+int(numero2)

def concatena(nome, sobrenome):
    return str(nome)+" "+str(sobrenome)

def fotosensor(velocidade):
    velocidade=int(velocidade)
    if velocidade <=60:
        return str(velocidade)+'km/h - não multa'
    elif velocidade >60 and velocidade <=80:
        return str(velocidade)+'km/h - multa leve'
    elif velocidade >80 and velocidade <=100:
        return str(velocidade)+'km/h - multa média'
    elif velocidade >100:
        return str(velocidade)+'km/h - multa grave'
    return 0

def execute(numero):
    lista=[]
    contador=0
    while contador<numero:
        velocidade=numeroaleatorio()
        print(fotosensor(velocidade))
        aguardando()
        contador=contador+1

    return 'Finalizado'
