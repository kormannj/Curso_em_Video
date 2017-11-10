real = float(input('Quanto dinheiro você tem na carteira? R$ '))
cotacao_dolar = 3.27
dolar = real / cotacao_dolar

print('Com R${:.2f} você conseguirá comprar US${:.2f}.'.format(real, dolar))