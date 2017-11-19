#Conversão de número inteiro para binário, octal ou hexadecimal
numero = int(input('Informe um número inteiro: '))
base = int(input('''Deseja converter para:
1) Binário
2) Octal
3) Hexadecimal
Opção: '''))

if base == 1:
    print('O número {} convertido para binário é {}.'.format(numero, bin(numero)[2:]))
elif base == 2:
    print('O número {} convertido para octal é {}.'.format(numero, oct(numero)[2:]))
elif base == 3:
    print('O número {} convertido para hexadecimal é {}.'.format(numero, hex(numero)[2:]))
else:
    print('Você informou uma opção inválida.')