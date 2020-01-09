# CUSTO DA VIAGEM
# Desenvolva um programa que pergunte a distancia de uma viagem em KM. Calcule o preço da passagem, cobrando R$0,50 por
# km para viagens de ate 200km e R$0,45 para viagens mais longas.

distancia = float(input('Informe a distancia da sua viagem: '))
print('Voce esta prestes a começar uma viagem de {}KM'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
