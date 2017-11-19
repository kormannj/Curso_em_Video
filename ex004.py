n = input("Digite um valor: ")
print('O tipo primitivo desse valor é ', type(n))
print('Só tem espaços?', n.isspace())
print('É um número?', n.isnumeric())
print('É alfabético?', n.isalpha())
print('É alfanumérico?', n.isalnum())
print('Está em maiúsculas?', n.isupper())
print('Está em minúsculas?', n.islower())
print('Está capitalizada', n.istitle())

print('Apenas caracteres decimais?', n.isdecimal())
print('É um identificador?', n.isidentifier()) #
print('isdigit', n.isdigit())
print('isprintable', n.isprintable())

