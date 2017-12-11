#Cálculo do fatorial de um número com função
from math import factorial

num = int(input('Digite um número: '))
fatorial = factorial(num)
print('O fatorial do número {} é {}.'.format(num, fatorial))