#Média de notas x resultado
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('Sua média foi {:.1f}. Você foi reprovado. Estude mais, pequeno gafanhoto!'.format(media))
elif media >= 5 and media < 7:
    print('Sua média foi {:.1f}. Você está de recuperação. Se esforce mais um pouco que você está quase lá!'.format(media))
else:
    print('Parabéns, pequeno gafanhoto! Sua média foi {:.1f} e você foi aprovado!!!'.format(media))