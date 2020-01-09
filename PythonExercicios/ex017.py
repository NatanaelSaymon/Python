# Faca um programar que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo. Calcule e mostre
# o comprimento da hipotenusa
# Formula para se calcular a hipotenusa: (cateto-oposto ** 2 + cateto-adjacente ** 2) ** (1/2)

ca = float(input('Comprimento do cateto oposto: '))
co = float(input('Comprimento do cateto adjacente :'))

hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))

