#Exemplo - 04 while contado

cont = 1

while cont <= 3:
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    print('Media = ', (n1 + n2) / 2)
    cont = cont + 1 #atualiza a variavel usada na condição
