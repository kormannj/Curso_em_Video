#Preço do produto conforme a forma de pagamento
print('{:=^40}'.format(' LOJAS GUANABARA ')) #Centralizado com 40 caracteres e completando com '='
preco_produto = float(input('Informe o preço do produto: '))
forma_pagto = int(input('''Informe a condição de pagamento desejada:
[1] À vista em dinheiro/cheque
[2] À vista no cartão
[3] Até 2x no cartão
[4] 3x ou mais no cartão
Opção: '''))

if forma_pagto == 1:
    preco_final = preco_produto - preco_produto * 10 / 100
elif forma_pagto == 2:
    preco_final = preco_produto - preco_produto * 5 / 100
elif forma_pagto == 3:
    num_parcelas = 2
    preco_final = preco_produto
    valor_parcela =  preco_produto / num_parcelas
    texto = 'SEM JUROS'
elif forma_pagto == 4:
    num_parcelas = int(input('Quantas parcelas? '))
    preco_final = preco_produto + preco_produto * 20 / 100
    valor_parcela = preco_produto / num_parcelas
    texto = 'COM JUROS'
else:
    print('Opção inválida!')

if forma_pagto in (1, 2, 3, 4):
    if forma_pagto in (3, 4):
        print('Sua compra será parcelada em {}X de R${:.2f} {}.'.format(num_parcelas, valor_parcela, texto))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco_produto, preco_final))