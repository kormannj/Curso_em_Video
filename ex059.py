#Menu com operações matemáticas sobre dois números
sair = False
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

while not sair:
    print('''\nMENU
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    ''')
    opcao_ok = False
    while not opcao_ok:
        opcao = int(input('Informe a opção desejada: '))
        if opcao not in range(1, 6):
            print('Opção inválida! Digite um valor entre 1 e 5.')
        else:
            opcao_ok = True

    if opcao == 1:
        soma = numero1 + numero2
        print('Você escolheu somar os números e o resultado é {}.'.format(soma))
    elif opcao == 2:
        multiplicacao = numero1 * numero2
        print('Você escolheu multiplicar os números e o resultado é {}.'.format(multiplicacao))
    elif opcao == 3:
        maior = numero1
        if numero2 > numero1:
            maior = numero2

        if numero2 == numero1:
            print('Você escolheu saber o maior número, mas ambos são iguais.')
        else:
            print('O maior número informado é {}.'.format(maior))
    elif opcao == 4:
        print('Ok, você poderá digitar novos números.\n')
        numero1 = int(input('Digite o primeiro número: '))
        numero2 = int(input('Digite o segundo número: '))
    else:
        print('Você escolheu sair do programa.')
        sair = True

    print('')