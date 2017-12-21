#While com condição de parada
num = qt_num = soma = 0
while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break

    qt_num += 1
    soma += num

print(f'A soma dos {qt_num} números é {soma}.')
