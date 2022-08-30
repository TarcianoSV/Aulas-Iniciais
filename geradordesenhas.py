'''Gerador de senhas( utilizando digitos de Cpf + Cep + Celular'''

senhas=[]
while True:
    numerocpf = input ('Insira seu CPF:')

    numerocep = input ('Insira seu CEP:')

    numerocel = input ('Insira seu Celular:')

    senha=numerocpf[:4]+numerocep[-2:]+numerocel[-4:]
    senhas.append(senha)

    print(senhas)
