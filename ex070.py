#Cadastro de produtos com estatísticas no fim
print('-' * 30)
print('{:^30}'.format('LOJA SUPER BARATÃO'))
print('-' * 30)

continua = 'S'
prod_mais_barato = ''
preco_mais_barato = total_gasto = cont_prod_mais1000 = 0

while continua == 'S':
    produto = input('Produto: ')
    preco = float(input('Preço: '))

    if prod_mais_barato == '' or preco < preco_mais_barato:
        preco_mais_barato = preco
        prod_mais_barato = produto

    total_gasto += preco

    if preco > 1000:
        cont_prod_mais1000 += 1

    while True:
        continua = input('Deseja continuar (S/N)? ').strip().upper()[0]
        if continua in 'SN':
            break

print('{:-^30}'.format(' FIM DO PROGRAMA '))
print(f'Total gasto na compra: R${total_gasto:.2f}.')
print(f'{cont_prod_mais1000} produtos custam mais de R$1.000,00.')
print(f'O produto mais barato é {prod_mais_barato} e custa R${preco_mais_barato:.2f}.')
