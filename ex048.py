#Somar ímpares múltiplos de 3 no intervalo
#Maneira 1
soma = 0
qt_itens = 0
for cont in range(1, 501, 2):
    if cont % 3 == 0:
        print(cont, end=' ')
        qt_itens += 1
        soma += cont

print('\nA soma dos {} valores é {}.\n'.format(qt_itens, soma))

#Maneira 2
soma = 0
qt_itens = 0
for cont in range(3, 501, 6):
    print(cont, end=' ')
    qt_itens += 1
    soma += cont

print('\nA soma dos {} valores é {}.'.format(qt_itens, soma))