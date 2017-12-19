#Leitura de cadastro de pessoas
print('-' * 30)

continua = 'S'
pessoas_mais18 = qt_homens = mulheres_menos20 = 0
while continua == 'S':
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in ('M', 'F'):
        sexo = input('Digite o sexo (M/F): ').strip().upper()[0]

    if idade > 18:
        pessoas_mais18 += 1
    if sexo == 'M':
        qt_homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos20 += 1

    print('-' * 30)
    continua = ' '
    while continua not in ('S', 'N'):
        continua = input('Deseja continuar (S/N)? ').strip().upper()[0]

print('====== FIM DO PROGRAMA ======')
print(f'Total de pessoas com mais de 18 anos: {pessoas_mais18}.')
print(f'Ao todo temos {qt_homens} homens cadastrado(s).')
print(f'Temos {mulheres_menos20} mulheres com menos de 20 anos.')
