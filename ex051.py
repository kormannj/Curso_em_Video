#Progressão aritmética pedindo primeiro termo e a razão

#Maneira 1
prim_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
pa = prim_termo

print('Os dez primeiros termos da PA são: {}'.format(pa), end=' ')
for cont in range(1, 10):
    pa += razao
    print(pa, end=' ')

print('\n')
#Maneira 2
decimo_termo = prim_termo + (10 - 1) * razao

print('Os dez primeiros termos da PA são: ', end='')
for cont in range(prim_termo, decimo_termo + 1, razao):
    print(cont, end=' ')