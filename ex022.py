nome = input('Digite seu nome completo: ')
n_mai = nome.upper()
n_min = nome.lower()
qt_letras_sem_espaco = len(nome) - nome.count(' ')
nome_separado = nome.split()
qt_letras_prim_nome = len(nome_separado[0])

print('Nome: {0}, Maiúsculo: {1}, Minúsculo: {2}, Qt Letras sem Espaço: {3}, Qt Letras Primeiro Nome: {4}'.format(nome, n_mai, n_min, qt_letras_sem_espaco, qt_letras_prim_nome))
