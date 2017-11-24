#Checar de uma frase forma um palíndromo
frase_original = input('Digite uma frase: ').upper()
frase_sem_espacos = frase_original.replace(' ', '')

frase_invertida = frase_sem_espacos[::-1]

print('O inverso de {} é {}.'.format(frase_sem_espacos, frase_invertida))
if frase_sem_espacos == frase_invertida:
    print('A frase {} é um palíndromo.'.format(frase_original.upper()))
else:
    print('A frase {} não é um palíndromo.'.format(frase_original.upper()))