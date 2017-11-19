#reajuste de salário
salario = float(input('Digite o seu salário: '))

if salario > 1250:
    reajuste = 10
    salario = salario * 1.10
else:
    reajuste = 15
    salario = salario * 1.15

print('Seu salário sofreu um reajuste de {}% e passou para R${:.2f}'.format(reajuste, salario))
