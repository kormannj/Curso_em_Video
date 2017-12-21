#Progressão aritmética pedindo primeiro termo e a razão, usando somente WHILE e solicitando mais quantos termos
#Maneira 2
prim_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
pa = prim_termo
decimo_termo = prim_termo + (10 - 1) * razao
cont_total = 10

print('Os dez primeiros termos da PA são: ', end='')
while pa != (decimo_termo + razao):
    print(pa, end=' ')
    pa += razao

pa -=razao
qt_termos = 1
while qt_termos != 0:
    print('\n')
    qt_termos = int(input('Você deseja ver mais quantos termos? (tecle 0 para finalizar) '))
    if qt_termos != 0:
        cont = 1
        cont_total += qt_termos
        while cont <= qt_termos:
            pa += razao
            cont += 1
            print(pa, end=' ')

print('Progressão finalizada com {} termos.'.format(cont_total))
