# DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZAO DE UMA PA (PROGRESSAO ARITMETICA). NO FINAL, MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO.
# PA ( ONDE O PRIMEIRO ELEMENTO É 1 A RAZÃO(PUL0) É 10.

print('=' * 10)
print('10 TERMOS DE UMA PA')
print('=' * 10)
p = int(input('Primeiro termos: '))
r = int(input('Razão: '))
d = p + (10 - 1) * r
for c in range(p, d + r, r):
    print(c, end=' ')
print('ACABOU!')