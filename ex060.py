#Cálculo do fatorial de um número com WHILE
num = int(input('Digite um número: '))
num_orig = num

if num <= 0:
    print('O número deve ser maior que zero.')
else:
    fatorial = 1
    while num >= 1:
        fatorial *= num
        num -= 1

print('O fatorial do número {} é {}.\n'.format(num_orig, fatorial))
