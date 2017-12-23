#Progressão aritmética pedindo primeiro termo e a razão, usando WHILE

#Maneira 1
prim_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
pa = prim_termo

print('Os dez primeiros termos da PA são: {}'.format(pa), end=' ')
cont = 2
while cont <= 10:
    pa += razao
    cont += 1
    print(pa, end=' ')
    
