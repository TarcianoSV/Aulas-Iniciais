medida = float(input('Uma distancia em metros: '))
cm = medida *100
mm = medida *1000
print('A medida de {:.0f} m corresponde a {:.0f} cm e {:.0f} mm '.format(medida, cm ,mm))

'''conversor de metros simples'''

real = float(input('Quanto Dinheiro você tem na carteira? R$= '))
dolar = real / 5.14
euro = real / 5.16
yen = real / 0.04
libra = real / 5.96
print('Com R$ {:.2f} você pode comprar US$ {:.2f} Dolares'.format(real, dolar))
print('Com R$ {:.2f} você pode comprar € {:.2f} Euros'.format(real, euro))
print('Com R$ {:.2f} você pode comprar ¥ {:.2f} Yens'.format(real, yen))
print('Com R$ {:.2f} você pode comprar £ {:.2f} Libras'.format(real, libra))

'''conversor de moedas real para Dolar,EURO,YEN e Libras cotação em 10/09/2022 (mudar para a cotação do dia)'''
'''(Ou usar Json pra puxar atraves de uma API cotação em tempo real)'''
