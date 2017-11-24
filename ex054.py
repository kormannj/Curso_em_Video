#Contar quantos atingiram a maioridade
from datetime import datetime

cont_maior_idade = 0
cont_menor_idade = 0
for cont in range(1, 8):
    ano_nascimento = int(input('Em que ano a {}a. pessoa nasceu? '.format(cont)))
    if datetime.today().year - ano_nascimento >= 21:
        cont_maior_idade += 1
    else:
        cont_menor_idade += 1

print('Das sete pessoas, {} já atingiram a maioridade e {} ainda não.'.format(cont_maior_idade, cont_menor_idade))