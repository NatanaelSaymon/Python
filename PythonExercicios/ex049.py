# REFAÇA O DESAFIO 009, MOSTRANDO A TABUADA DE UM NUMERO QUE O USUARIO ESCOLHER, SÓ QUE AGORA UTILIZANDO UM LAÇO FOR.

print('-=' * 20)
num = int(input('Digite um numero para ver a sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num * c))
print('-=' * 20)