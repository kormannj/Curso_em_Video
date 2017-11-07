#Preço da passagem
distancia = float(input('Qual a distância a ser percorrida na viagem? '))

if distancia <= 200:
    passagem = distancia * 0.5
else:
    passagem = distancia * 0.45

print('O valor da passagem é {:.2f}'.format(passagem))
