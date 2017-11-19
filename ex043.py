#Cálculo e classificação de IMC
peso = float(input('Informe o seu peso: '))
altura = float(input('Informe sua altura em metros: '))

imc = peso / altura ** 2
if imc < 18.5:
    resultado = 'abaixo do peso'
elif imc < 25:
    resultado = 'com o peso ideal'
elif imc < 30:
    resultado = 'com sobrepeso'
elif imc < 40:
    resultado = 'com obesidade'
else:
    resultado = 'com obesidade mórbida'

print('Seu IMC é de {:.2f}, o que significa que você está {}.'.format(imc, resultado))