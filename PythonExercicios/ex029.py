# RADAR ELETRONICO
# escreva um programa que leia a velocidade de umu carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 cada km acima do limite.

velocidade = float(input('Qual a velocidade atual do carro: '))
if velocidade > 80:
    print('ALERT! Você foi Multado!! Sua velocidade ultrapassou o limite de 80km/h')
    multa = (velocidade - 80) * 7
    print('Voce deverar pagar uma multda de R${}'.format(multa))
print('Tenha um bom dia! E dirija com cuidado.')