#Escreva um programa em Python para calcular o valor de uma
#prestação em atraso (prestacao). Para isso, obtenha o valor da
#prestação (valorPrestacao), a porcentagem de multa pelo atraso
#(multa) e a quantidade de dias de atraso (qtdeDias). Calcular e mostrar
#o valor da prestação atualizado, sabendo que:
#prestacao=valorPrestacao+(valorPrestacao*(multa/100)*qtdeDias)

valorprestacao = float(input('Digite o valor da sua prestação: '))
qtdedias = int(input('Quantidade de dias em atraso? '))
multa = 5
prestacao = valorprestacao + (valorprestacao * (multa / 100) * qtdedias)
print('O valor da sua prestação é R${}'.format(prestacao))