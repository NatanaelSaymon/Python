# Escreva um programa que pergunte a quantidade de KM percorrido por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado.

km = float(input('Informe a quantiade de km percorrido: KM'))
dias = int(input('Digite a quantidade de dias alugado: '))
pago = (km * 0.15) + (dias * 60)
print('Valor a pagar R${}'.format(pago))