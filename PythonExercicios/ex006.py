# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.

num = int(input('Digite um numero: '))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2) #raiz quadrada
print('O dobre de {} vale {}.'.format(num, dobro))
print('O triplo de {} vale {}.'.format(num, triplo))
print('A raiz quadrada de {} vale {:.2f}.'.format(num, raiz))
