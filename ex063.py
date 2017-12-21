#Mostrar n elementos da Sequência de Fibonacci com WHILE
qt_elementos = int(input('Quantos elementos da Sequência de Fibonacci você deseja mostrar? '))

num1 = 0
num2 = 1
cont = 1

print('Sequência: ', end='')

while cont != qt_elementos + 1:
    if cont == 1:
        print(num1, end=' ')
    elif cont == 2:
        print(num2, end=' ')
    else:
        soma = num1 + num2
        print(soma, end=' ')
        num1 = num2
        num2 = soma
    cont += 1
