nome = input('Digite seu nome completo: ')
splitado = nome.split()
prim_nome = splitado[0]
ult_nome = splitado[len(splitado) - 1]

print('Primeiro nome: {}, último nome: {}'.format(prim_nome, ult_nome))