# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria
# de acordo com a idade. Considere o ano atual 2018.
# Até 9 anos: mirim
# Até 14 anos: infantil
# Até 19 anos: Junior
# Até 20 anos: Sênior
# Acima: Master

print('-=' * 20)
print('Confederação Nacional de Natação.')
print('Ate 9 anos: MIRIM')
print('Até 14 anos: INFANTIL')
print('Até 19 anos: JUNIOR')
print('Até 20 anos: SENIOR')
print('Acima de 20 anos: MASTER')
print('-=' * 20)
ano = int(input('Digite o ano do seu nascimento: '))
idade = 2018 - ano
if idade > 5 and idade <= 9:
    print('Você tem {} anos e a sua categoria é Mirim.'.format(idade))
elif idade > 9 and idade <= 14:
    print('Você tem {} anos e a sua categoria é Infantil.'.format(idade))
elif idade > 14 and idade <= 19:
    print('Você tem {} anos e a sua categoria é Junior.'.format(idade))
elif idade == 20:
    print('Você tem {} anos e a sua categoria é Sênior.'.format(idade))
elif idade > 20:
    print('Você tem {} anos e a sua categoria é Master.'.format(idade))


