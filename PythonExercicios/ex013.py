# Faca um algortitmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento.

salario = float(input('Digite o valor do seu salario: R$'))

novosalario = salario + (salario * 15 / 100)

print('Com o aumento de 15%, o seu salario que era {} passou a ser {:.2f}'.format(salario, novosalario))