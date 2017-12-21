#Cadastro de pessoas com totalização de informações
print('-' * 30)
print('{:^30}'.format('CADASTRE UMA PESSOA'))
#Leitura de cadastro de pessoas
print('-' * 30)

pessoas_mais18 = qt_homens = mulheres_menos20 = 0
continua = 'S'

while continua == 'S':
    while True:
        idade = int(input('Digite a idade: '))
        if idade >= 0:
            break

    while True:
        sexo = input('Digite o sexo (M/F): ').strip().upper()[0]
        if sexo in 'MF':
            break

    if idade > 18:
        pessoas_mais18 += 1
    if sexo == 'M':
        qt_homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos20 += 1

    print('-' * 30)

    while True:
        continua = input('Deseja continuar (S/N)? ').strip().upper()[0]
        if continua in 'SN':
            break

print('{:=^30}'.format(' FIM DO PROGRAMA '))
print(f'Total de pessoas com mais de 18 anos: {pessoas_mais18}.')
print(f'Ao todo temos {qt_homens} homens cadastrado(s).')
print(f'Temos {mulheres_menos20} mulheres com menos de 20 anos.')
