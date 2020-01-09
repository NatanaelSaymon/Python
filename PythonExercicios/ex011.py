# Faca um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria
# para pinta-la, sabendo que cada litro pinta uma area de 2 metros quadrados.

largura = float(input('Digite a largura da sua parede: '))
alt = float(input('Digite a altura da sua parede: '))
area = largura * alt
tinta = area / 2
print('A sua parede tem a dimensão de {}x{} e a sua area é de {}m²'.format(largura, alt, area))
print('Para pintar a sua parede vai ser necessario {}l de tinta'.format(tinta))