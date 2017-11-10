import math

angulo = float(input('Informe o ângulo: '))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('Para o ângulo {}, o seno é {:.2f}, o coseno é {:.2f} e a tangente é {:.2f}'.format(angulo, seno, coseno, tangente))