#Tabuada de vários números com condição de parada
while True:
    num = int(input('Quer ver a tabuada de qual valor? (número negativo encerra) '))
    if num < 0:
        break

    print('-' * 33)
    for cont in range(1, 11):
        print(f'{num} x {cont} = {num * cont}')
    print('-' * 33)

print('PROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE!')
