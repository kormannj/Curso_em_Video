#Classificação de pessoas
soma_idade = 0
homem_mais_velho = ''
cont_menor_vinte = 0
for cont in range(1, 5):
    nome = input('Nome da {}a. pessoa: '. format(cont))
    idade = int(input('Idade da {}a. pessoa: '.format(cont)))
    sexo = input('Sexo da {}a. pessoa: '.format(cont)).upper()

    soma_idade += idade
    if sexo == 'M':
        if homem_mais_velho == '':
            homem_mais_velho = nome
            idade_mais_velho = idade
        elif idade > idade_mais_velho:
            homem_mais_velho = nome
            idade_mais_velho = idade
    elif idade < 20:
        cont_menor_vinte += 1

media_idade = soma_idade / 4
print('A média de idade do grupo é {:.2f}; o homem mais velho é {}, com {} anos; {} mulheres têm menos de 20 anos.'.format(media_idade, homem_mais_velho, idade_mais_velho, cont_menor_vinte))
