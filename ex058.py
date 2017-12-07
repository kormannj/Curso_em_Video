#Condição: tentar até acertar um número randômico entre 0 e 10
from random import randint

numero = randint(0, 10)
acertou = False
palpites = 0

while not acertou:
    chute = int(input('Tente adivinhar qual o número sorteado entre 0 e 10: '))
    palpites += 1
    if chute == numero:
        acertou = True
    else:
        if chute < numero:
            print('O número é maior. Tente novamente.')
        else:
            print('O número é menor. Tente novamente.')

print('Parabéns! Você acertou em {} palpites!'.format(palpites))