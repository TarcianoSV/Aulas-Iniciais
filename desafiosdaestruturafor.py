from time import sleep

for c in range (10,-1, -1):
    sleep(1)
    print(c)
print('Feliz Ano Novo!!')

'''contagem regressiva de ano novo, com intervalo de um segundo'''


for c in range (0,51, 2):
    print(c)
''' contado de 0 a 50 só os numeros pares '''

num = int(input('Digite um numero pra ver sua tabuada:'))
print('-' * 12)
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10, num*10))
print('-' * 12)
'''tabuada simples'''


tabuada=int(input("Tabuada do numero: "))

for count in range(10):
    print ("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)))
    
'''tabuada simplificada usando FOR''' Observação(Procurar nos exercicios de While a tabuada usando While)
