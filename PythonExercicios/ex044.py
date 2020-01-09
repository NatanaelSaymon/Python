# Crie um programa que faca o computador jogar JOKENPô com voce.

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções: 
[ 0 ] Pedra
[ 1 ] Papel
[ 3 ] Tesoura''')
jogador = int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou : {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: # computador jogou PEDRA
    if jogador == 0: # jogador jogou PEDRA
        print('EMPATE!')
    elif jogador == 1: # jogador jogou PAPEL
        print('JOGADOR VENCEU!')
    elif jogador == 2: # jogador jogou TESOURA
        print('COMPUTADOR VENCEU!')
    else:
        print('Jogada INVALIDA!')
elif computador == 1: # computador jogou PAPEL
    if jogador == 0: # jogador jogou PEDRA
        print('COMPUTADOR VENCEU!')
    elif jogador == 1: # jogador jogou PAPEL
        print('EMPATE!')
    elif jogador == 2: # jogador jogou TESOURA
        print('JOGADOR VENCEU!')
    else:
        print('Jogada INVALIDA!')
elif computador == 2: # computador jogou TESOURA
    if jogador == 0: # jogador jogou PEDRA
        print('JOGADOR VENCEU!')
    elif jogador == 1: # jogador jogou PAPEL
        print('COMPUTADOR VENCEU!')
    elif jogador == 2: # jogador jogou TESOURA
        print('EMPATE!')
    else:
        print('Jogada INVALIDA!')


