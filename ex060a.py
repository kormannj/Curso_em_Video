#Cálculo do fatorial de um número com FOR
num = int(input('Digite um número: '))
num_orig = num

if num <= 0:
    print('O número deve ser maior que zero.')
else:
    fatorial = 1
    for num in range(num, 1, -1):
        fatorial *= num

print('O fatorial do número {} é {}.\n'.format(num_orig, fatorial))