from math import hypot

cat_oposto = float(input('Informe o comprimento do cateto oposto: '))
cat_adjacente = float(input('Informe o comprimento do cateto adjacente: '))
hipotenusa = hypot(cat_oposto, cat_adjacente)

print('O cateto oposto é {:.2f}, o cateto adjacente é {:.2f} e a hipotenusa calculada é {:.2f}.'.format(cat_oposto, cat_adjacente, hipotenusa))