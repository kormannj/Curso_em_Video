altura = float(input('Informe a altura da parede: '))
largura = float(input('Informe a largura da parede: '))
cobertura_lata = 2
area_parede = altura * largura
quantidade_latas = area_parede / cobertura_lata

print('A área total a ser pintada é de {:.2f}m2 e você precisará de {:.2f} latas de tinta para cobrir a parede.'.format(area_parede, quantidade_latas))