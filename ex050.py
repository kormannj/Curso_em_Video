#Laço para pedir seis números e somar somente os pares
soma = 0
qt_pares = 0
for cont in range(0, 6):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma += numero
        qt_pares += 1

print('Foram digitados {} números pares e a soma deles é {}.'.format(qt_pares, soma))