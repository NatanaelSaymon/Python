# Crie um programa em python que leia quanto dinheiro um pessoa tem na carteira e mostre quantos dolares ela pode comprar.

# considere US$1.00 = R$3.72

real = float(input('Quanto de dinheiro voce tem na carteira: R$'))
dolar = real / 3.72
print('Com R${:.2f} voce  pode comprar US${:.2f}'.format(real, dolar))