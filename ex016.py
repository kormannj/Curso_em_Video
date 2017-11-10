from math import trunc

numero = float(input('Digite um número com casas decimais: '))
truncado = trunc(numero)

print('O número informado foi {} e a sua parte inteira é {}'.format(numero, truncado))

#Também é possível obter o mesmo resultado usando int(numero), em vez de importar um módulo/métodos.