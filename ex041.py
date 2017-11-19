#Categorização de atletas conforme a idade
from datetime import date

ano_nascimento = int(input('Informe o seu ano de nascimento: '))
idade = date.today().year - ano_nascimento

if idade <= 9:
    categoria = 'MIRIM'
elif idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JUNIOR'
elif idade <= 25:
    categoria = 'SENIOR'
else:
    categoria = 'MASTER'

print('Sua idade é {} e você se enquadra na categoria {}.'.format(idade, categoria))