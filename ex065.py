#Ler n números, apresentando sua média e o menor e maior números usando WHILE
cont = soma = 0

while True:
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
    while True:
        continua = input('Deseja continuar (S/N)? ').strip().upper()[0]
        if continua in 'SN':
            break
    if continua == 'N':
        break

media = soma / cont
print('Foram informados {} números. A média deles é {:.2f}, o menor é {} e o maior é {}.'.format(cont, media, menor, maior))
