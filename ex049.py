#Tabuada com uso de laço
numero = int(input('Digite um número: '))

print('A tabuada de {} é:'.format(numero))
print('='*20)

for cont in range(1, 11):
    print('{} x {:2} = {:3}'.format(numero, cont,  numero * cont))

print('='*20)
