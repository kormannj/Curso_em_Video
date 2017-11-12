#As retas formam um triângulo?
from math import fabs

r1 = int(input('Informe o valor da primeira reta: '))
r2 = int(input('Informe o valor da segunda reta: '))
r3 = int(input('Informe o valor da terceira reta: '))

if ((r1 < r2 + r3) and (r1 > fabs(r2 - r3))) or ((r2 < r1 + r3) and (r2 > fabs(r1 - r3))) or ((r3 < r1 + r2) and (r3 > fabs(r1 - r2))):
    print('Os valores informados formam um triângulo.')
else:
    print('Os valores informados não formam um triângulo.')