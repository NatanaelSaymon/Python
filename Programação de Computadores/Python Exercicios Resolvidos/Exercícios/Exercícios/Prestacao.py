#Escreva um programa em Python para calcular o valor de uma prestaçãobem atraso.
#Para isso, obtenha o valor da prestação (valorPrestacao),
#a porcentagem de multa pelo atraso (multa), e a quantidade de dias de atraso(qtdeDias)
#Calcular e mostrar o valor da prestação atualizado, sabendo que:
#prestacao =valorPrestacao+(valorPrestaca*(multa/100)*qtdeDias)




valorPrestacao = float(input("Informe o valor da prestação: "))
multa = int(input("Informe porcentagem de multa pelo atraso: "))
qtdeDias = int(input("Informe a quantidade de dias em atraso: " ))

prestacao = (valorPrestacao+(valorPrestacao*(multa/100)*qtdeDias))

print("O valor da prestação atualizado é: ", prestacao)
