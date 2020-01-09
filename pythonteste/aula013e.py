# Inserindo valores de 0 ate 5 ou mais e fazendo a soma dos numeros digitados

s = 0
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    s = s + n
print('A soma de todos os valores digitados foi: {}'.format(s))
print('Fim')
