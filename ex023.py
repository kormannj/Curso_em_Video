numero = int(input('Digite um número entre 0 e 9999: '))
num_string = str(numero).zfill(4) #Resolvendo com um método do Python para jogar zeros à esquerda.

print('Unidade: ', num_string[3])
print('Dezena: ', num_string[2])
print('Centena: ', num_string[1])
print('Milhar: ', num_string[0])

#Resolvendo com o uso da matemática.
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('Unidade: ', u)
print('Dezena: ', d)
print('Centena: ', c)
print('Milhar: ', m)
