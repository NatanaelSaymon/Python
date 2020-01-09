# Enquanto o usuario não digitar ZERO (0) o programa vai continuar:

n = 1
pares = 0
impares = 0
while n != 0: # Condição de parada!
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
print('Voce digitou {} numeros PARES e {} numeros IMPARES. '.format(pares, impares))
print('Fim')