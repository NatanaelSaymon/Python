#Crie um programa em Python que solicite ao usuário a sua idade
#expressa em anos, meses e dias (variáveis separadas). Calcule e
#mostre a idade expressa apenas em dias. Para isso considere 1 ano =
#365 dias, 1 mês = 30 dias.

anos = int(input('Digite a sua idade: '))
mes = 30
dias = anos * 365
print('Sua idade representada em dias é {}.'.format(dias))