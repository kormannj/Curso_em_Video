#Limite de velocidade
velocidade = float(input('Qual a velocidade do veículo? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você foi multado. O valor a pagar é {:.2f}'.format(multa))
