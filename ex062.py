#Progressão aritmética pedindo primeiro termo e a razão, usando somente WHILE e solicitando mais quantos termos

#Maneira 1
prim_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
pa = prim_termo
cont_total = 10

print('Os dez primeiros termos da PA são: {}'.format(pa), end=' ')
cont = 2
while cont <= 10:
    pa += razao
    cont += 1
    print(pa, end=' ')

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