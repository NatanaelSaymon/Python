# JOGO DA ADIVINHAÇÃO!
# Escreva um programa que faca o computador "pensar" em um numero inteiro entre 0 e 5 e peça o usuario tentar
# descobrir qual foi o numero escolhido pelo computador. O programa deverá escrever na tela se o usuario venceu ou perdeu.

import random # gera um numero aleatorio
computador = random.randint(0, 10) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero pensei: '))
if jogador == computador:
    print('PARABENS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no numero {}.'.format(computador, jogador))
