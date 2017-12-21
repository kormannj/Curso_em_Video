#Simulação de saque em caixa eletrônico
print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)

print('Notas disponíveis para saque: R$50, R$20, R$10 e R$1.')
valor_saque = int(input('Qual o valor a ser sacado? '))

notas50 = valor_saque // 50
valor_saque -= (notas50 * 50)
notas20 = valor_saque // 20
valor_saque -= (notas20 * 20)
notas10 = valor_saque // 10
valor_saque -= (notas10 * 10)
notas1 = valor_saque
valor_saque = 0

if notas50 > 0:
    print(f'Total de {notas50} cédulas de R$50')
if notas20 > 0:
    print(f'Total de {notas20} cédulas de R$20')
if notas10 > 0:
    print(f'Total de {notas10} cédulas de R$10')
if notas1 > 0:
    print(f'Total de {notas1} cédulas de R$1')
