#exemplo 1 - aula 07

#entrada de dados
gravidade = int(input("Digite a gravidade das multas"))
qtde = int(input("Digite a quantidade de multas"))

#processamento e saída
if gravidade == 1:
    print("Valor a pagar: ",qtde*53.2,"\nTotal de pontos:",qtde*3)
elif gravidade == 2:
    print("Valor a pagar: ",qtde*85.13,"\nTotal de pontos:",qtde*4)
elif gravidade == 3:
    print("Valor a pagar: ",qtde*127.69,"\nTotal de pontos:",qtde*5)
elif gravidade == 4:
    print("Valor a pagar: ",qtde*574.62,"\nTotal de pontos:",qtde*7)
else:
    print("Gravidade não existe")
print("exemplo terminou")
