#Leitura de cadastro de pessoas
continua = 'S'
mais18 = qt_homens = mulheres_menos20 = 0
while continua == 'S':
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo (M/F): ').strip().upper()[0]
    continua = input('Deseja continuar (S/N)? ').strip().upper()[0]
    mais18 = mais18 + 1 if idade > 18