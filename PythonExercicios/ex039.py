# Faca um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda
# vai se alistar ao serviço militar, se é a hora de se alistar ou seja passou do tempo do alistamento. Seu
# programa tbm devera mostrar o tempo que falta ou que passou do prazo.

from datetime import date
atual = date.today().year
nasci = int(input('Ano de nascimento: '))
idade = atual - nasci
print('Quem nasceu em {} tem {} ano(s) em {}.'.format(nasci, idade, atual))
if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} ano(s) para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento foi em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Voce já deveria ter se alistado há {} ano(s).'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
