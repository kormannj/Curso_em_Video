#Maior e menor pesos lidos - com lista
pesos = []
for cont in range(1, 6):
    peso = float(input('Qual o peso da {}a. pessoa? '.format(cont)))
    pesos.append(peso)

print('O menor peso informado foi {:.1f} e o maior foi {:.1f}'.format(min(pesos), max(pesos)))