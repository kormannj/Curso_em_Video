#Salário comporta a compra do imóvel?
valor_imovel = float(input('Valor do imóvel: '))
salario = float(input('Salário do comprador: '))
anos_financ = int(input('Em quantos irá pagar: '))

meses_financ = anos_financ * 12
parcela_mensal = valor_imovel / meses_financ
valor_maximo_mensal = salario * 0.3

if parcela_mensal > valor_maximo_mensal:
    print('O valor da prestação mensal é R${:.2f} e excede 30% do salário (R${:.2f}). O empréstimo não pode ser efetuado.'.format(parcela_mensal, valor_maximo_mensal))
else:
    print('Parabéns! Seu financiamento foi aprovado. O valor das parcelas será de R${:.2f}.'.format(parcela_mensal))