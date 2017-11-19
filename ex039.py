#Ano de nascimento x ano de alistamento militar
from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Informe o seu ano de nascimento: '))
idade = ano_atual - ano_nascimento

if idade == 18:
    print('Você deve se alistar nas forças armadas nesse ano.')
elif idade < 18:
    saldo = 18 - idade
    print('Falta(m) {} ano(s) para você se alistar nas forças armadas.'.format(saldo))
    print('Seu alistamento será em {}.'.format(ano_atual + saldo))
else:
    saldo = idade - 18
    print('Já passou/passaram {} ano(s) de você se alistar para as forças armadas.'.format(saldo))
    print('Seu ano de alistamento era {}.'.format(ano_atual - saldo))