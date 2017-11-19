#Ano bissexto com possibilidade de ler o ano atual
from datetime import date

ano = int(input('Que ano quer analisar? Informe 0 caso queira analisar o ano atual: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print('O ano {} informado é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
