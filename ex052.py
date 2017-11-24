#Determinar se o número informado é primo
numero = int(input('Digite um número maior que 1: '))

tot_divisoes = 0
if numero <= 1:
    print('Informe um número válido!')
else:
    for cont in range(1, numero + 1):
        if numero % cont == 0:
            tot_divisoes += 1
            print('\33[34m', end='')
        else:
            print('\33[31m', end='')
        print('{}'.format(cont), end=' ')

print('\n\33[mO número {} foi divisível {} vezes e, por isso, ele {} primo.'.format(numero, tot_divisoes, 'é' if tot_divisoes > 2 else 'não é'))