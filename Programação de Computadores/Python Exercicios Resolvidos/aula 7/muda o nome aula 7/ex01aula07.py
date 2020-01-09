#Um hotel cobra R$ 300,00 por diária por pessoa e mais uma
#taxa adicional de serviços. Se o número de diárias for menor
#que 15 a taxa é de R$ 20,00. Se o número de diárias for igual a
#15 a taxa é de R$ 14,00 e se o número for maior que 15 a taxa
#é de R$ 12,00.
#Faça um programa em Python que solicite o nome do cliente, a
#quantidade de pessoas e o número de diárias e mostre o nome
#e o total a pagar pelo cliente.

cli = str(input("Ola, qual o seu nome Sr. "))
pes = int(input("Sr.{} quantas pessoas vão se ospedar em nosso hotel? ".format(cli)))
dia = int(input("Sr. {} pretende ficar em nosso hotel por quanto tempo? ".format(cli)))
dir = 300 * pes

if dia < 15:
    print("Sr. {} sua diaria custara R$ {}".format(cli, dia * dir + (20 * dia * pes)))
elif dia == 15:
    print("Sr. {} sua diaria custara R$ {}".format(cli, dia * dir + (14 * dia * pes)))
elif dia >= 15:
    print("Sr. {} sua diaria custará R$ {}".format(cli, dia * dir + (12 * dia * pes)))
