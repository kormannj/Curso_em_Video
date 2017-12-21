#Jogo do Par ou ímpar
from random import randint

print('=-' * 12)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 12)
jogador_venceu = True
qt_vitorias = 0

while jogador_venceu:
    num_jogador = int(input('Digite um valor: '))
    while True:
        escolha = input('Par ou ímpar (P/I)? ').strip().upper()[0]
        if escolha in 'PI':
            break

    num_computador = randint(0, 10)
    soma = num_jogador + num_computador
    soma_eh_par = True if soma % 2 == 0 else False

    if (escolha == 'P' and soma_eh_par) or (escolha == 'I' and soma_eh_par == False):
        qt_vitorias += 1
    else:
        jogador_venceu = False

    print('-' * 50)
    print('Você jogou {} e o computador {}. Total de {} ... deu {}.'.format(num_jogador, num_computador, soma, 'PAR' if soma_eh_par else 'ÍMPAR'))
    print('-' * 50)
    print('Você {}.'.format('VENCEU' if jogador_venceu else 'PERDEU'))
    if jogador_venceu:
        print('Vamos jogar novamente ...')

print('GAME OVER! Você venceu {} {}.'.format(qt_vitorias, 'vez' if qt_vitorias == 1 else 'vezes'))
