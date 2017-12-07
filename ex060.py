#Cálculo do fatorial de um número
num = int(input('Digite um número: '))
num_orig = num

if num <= 0:
    print('O número deve ser maior que zero.')
else:
    cont = 0
    while num >= 1:
        if cont == 0:
            fatorial = num
        else:
            fatorial = fatorial * num

        cont += 1
        num -= 1

print('O fatorial do número {} é {}.'.format(num_orig, fatorial))