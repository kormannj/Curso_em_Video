#Pedro, papel, tesoura - Jokenpô
from random import choice
from time import sleep
from sys import exit

print('{:=^60}'.format(' JOKENPÔ - PEDRA, PAPEL, TESOURA '))
print('''\nSuas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
''')
escolha = int(input('Qual a sua escolha? '))

if escolha not in (0, 1, 2):
    print('Opção inválida!')
    exit()

opcoes = ['Pedra', 'Papel', 'Tesoura']
jogador = opcoes[escolha]
computador = choice(opcoes)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)

if jogador == computador:
    resultado = 'HOUVE EMPATE'
elif jogador == 'Pedra':
    if computador == 'Tesoura':
        resultado = 'JOGADOR VENCE'
    else:
        resultado = 'COMPUTADOR VENCE'
elif jogador == 'Papel':
    if computador == 'Pedra':
        resultado = 'JOGADOR VENCE'
    else:
        resultado = 'COMPUTADOR VENCE'
else:
    if computador == 'Papel':
        resultado = 'JOGADOR VENCE'
    else:
        resultado = 'COMPUTADOR VENCE'

print('-='*20)
print('O jogador jogou {} e o computador jogou {}.'.format(jogador, computador))
print('-='*20)
print(resultado)
