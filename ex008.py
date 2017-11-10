metros = float(input('Medida em metros: '))

kilometros = metros / 1000
hectometros = metros / 100
decametros = metros / 10
decimetros = metros * 10
centimetros = metros * 100
milimetros = metros * 1000

print('A medida de {0}m equivale a {1:.3f}km, {2:.3f}hm, {3:.3f}dam, {4:.0f}dm, {5:.0f}cm e {6:.0f}mm.'.format(metros, kilometros, hectometros, decametros, decimetros, centimetros, milimetros))