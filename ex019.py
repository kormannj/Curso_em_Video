from random import choice

aluno1 = input('Aluno 1: ')
aluno2 = input('Aluno 2: ')
aluno3 = input('Aluno 3: ')
aluno4 = input('Aluno 4: ')

lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(lista)

print('O aluno escolhido foi {}.'.format(escolhido))