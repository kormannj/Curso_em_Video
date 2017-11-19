#Condição: adivinhar o número randômico
from random import randint

numero = randint(0, 5)
chute = int(input('Tente adivinhar qual o número sorteado entre 0 e 5: '))

if chute == numero:
    print('Parabéns! Você acertou!')
else:
    print('Que pena! Você errou. O número era {}.'.format(numero))
