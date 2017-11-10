km = float(input('Qual a a quilometragem rodada? Km: '))
dias = int(input('Quantos dias o carro foi alugado? '))
valor_pagar = (60 * dias) + (km * 0.15)

print('O carro percorreu {:.2f}km e ficou alugado por {} dias. O preço a pagar pelo aluguel é de R${:.2f}'.format(km, dias, valor_pagar))