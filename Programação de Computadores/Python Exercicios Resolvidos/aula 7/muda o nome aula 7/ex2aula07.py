#Escreva um programa em Python que solicite ao usuário o
#código de origem de um produto e o seu custo. Calcule o
#mostre a nome da origem e o custo total do mesmo, de acordo
#com o seu fator de multiplicação.

codigo = int(input('Digite o codigo de origem do protudo: '))
custo = float(input('Informe o custo do protudo: '))
if codigo >= 1 and codigo <= 15:
    total=custo*2.05
    print('Origem Sul, custo total {:.2f}'.format(total))
elif codigo >= 16 and codigo<=25:
    total=custo*2.25
    print('Origem Norte, custo total {:.2f}'.format(total))
elif codigo >=26 and codigo <=35:
    total=custo*2.23
    print('Origem Leste, custo total {:.2f}'.format(total))
elif codigo >=36 and codigo <=45:
    total=custo*2.15
    print('Origem Oeste, custo total {:.2f}'.format(total))