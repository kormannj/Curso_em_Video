#Mostrar números pares entre 1 e 50

#Maneira 1
for cont in range(1, 51):
    if cont % 2 == 0:
        print(cont, end=' ')

print('\n')

#Maneira 2
for cont in range(2, 51, 2):
    print(cont, end=' ')