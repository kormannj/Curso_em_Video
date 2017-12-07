#Digitação de sexo M ou F
sexo = ' '

while sexo not in 'MF':
    sexo = input('Qual o seu sexo (M/F)? ').strip().upper()[0] #Estou eliminando espaços, colocando como maiúsculo e pegando apenas a primeira letra

print('O sexo informado é {}'.format(sexo))