#Ler n números somando-os e contando-os usando WHILE
num = cont = soma = 0
while num != 999:
    num = int(input('Digite um número inteiro (999 encerra o programa): '))
    if num != 999:
        cont += 1
        soma += num

print('Foram informados {} números e a soma deles é {}.'.format(cont, soma))
