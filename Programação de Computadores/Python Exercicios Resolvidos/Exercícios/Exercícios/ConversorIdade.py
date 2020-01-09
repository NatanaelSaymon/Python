
#Crie um programa  em Python  que solicite ao usuário a sua idade expressa
#em anos, meses e dias. Calcule e mostre a idade expressa apenas em dias
#Para isso considere 1 ano = 365 dias, 1 mes = 30 dias


anos = int(input("Informe a quantidade de anos: "))
meses = int(input("Informe a quantidade de meses: "))
dias = int(input("Informe a quantidade de dias: " ))

idade = (dias+(anos*365)+(meses*30))

print("Você tem: ", idade, "dias")
