#Maior e menor pesos lidos
for cont in range(1, 6):
    peso = float(input('Qual o peso da {}a. pessoa? '.format(cont)))
    if cont == 1:
        menor_peso = peso
        maior_peso = peso
    else:
        if peso < menor_peso:
            menor_peso = peso
        if peso > maior_peso:
            maior_peso = peso

print('O menor peso informado foi {:.1f} e o maior foi {:.1f}'.format(menor_peso, maior_peso))