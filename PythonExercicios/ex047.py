# CRIE UM PROGRAMA QUE MOSTRE NA TELA TODOS OS NUMEROS PARES QUE ESTÃO NO INTERVALO ENTRE 1 A 50.
s = 0
for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=' ')
print('fim')