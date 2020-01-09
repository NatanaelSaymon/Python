# Exemplo - 05 while condicional

soma = 0
cont = 0
resp = 's'
while resp == 's' or resp == 'S':
    n1 = float(input('Digite o primeiro numero: '))
    soma = soma + n1
    cont = cont + 1
    resp = input('Deseja cont...? (S/N)')
print('A media =', soma/cont)
    
