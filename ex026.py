frase = input('Digite uma frase: ').strip()

qt_letra_a = frase.upper().count('A')
prim_letra = frase.upper().find('A') + 1
ult_letra = frase.upper().rfind('A') + 1
print('A letra A aparece {} vezes. A primeira letra A apareceu na posição {} e a última letra A apareceu na posiição {}.'.format(qt_letra_a,prim_letra, ult_letra))

#for (letra in frase.upper() where letra == 'A'):