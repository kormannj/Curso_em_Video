#Checar se números são iguais ou qual é o maior
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

if num1 > num2:
    print('O primeiro número é maior do que o segundo.')
elif num2 > num1:
    print('O segundo número é maior do que o primeiro.')
else:
    print('Os dois números são iguais.')