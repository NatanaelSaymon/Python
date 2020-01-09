# AUMENTOS MULTIPLOS
# ESCREVA UM PROGRAMA QUE PERGUNTE O SALARIO DE UM FUNCIONARIO E CALCULE O VALOR DE SEU AUMENTO.
# PARA SALARIOS SUPERIOR A R$1250.00, CALCULE UM AUMENTO DE 10%. PARA OS INFERIORES OU IGUAIS, O AUMENTO É DE 15%.

salario = float(input('Informe o seu salario: R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('De acordo com o seu salario, voce obteve um aumento e o seu novo salario é R${:.2f}'.format(novo))