#Ler n números apresentando sua média e o menor e maior números usando WHILE
cont = soma = 0
continua = True

while continua:
    num = int(input('\nInforme um número: '))
    if cont == 0:
        menor = maior = num
    else:
        if num < menor:
            menor = num
        if num > maior:
            maior = num

    soma += num
    cont += 1
    continua = input('Deseja continuar (S/N)? ').strip().upper()
    if continua == 'N':
        continua = False

media = soma / cont
print('Foram informados {} números. A média deles é {:.2f}, o menor é {} e o maior é {}.'.format(cont, media, menor, maior))
