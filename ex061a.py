#Progressão aritmética pedindo primeiro termo e a razão, usando WHILE
#Maneira 2
prim_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

pa = prim_termo
decimo_termo = prim_termo + (10 - 1) * razao

print('Os dez primeiros termos da PA são: ', end='')
while pa != (decimo_termo + razao):
    print(pa, end=' ')
    pa += razao