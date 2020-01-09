#exemplo 2 - aula 7

#entrada de dados
salarioB = float(input("Digite o valor do salário base"))
tempo = int(input("Digite o tempo de serviço"))

#processamento
if salarioB > 1500:
    if tempo <= 3:
        salarioB = salarioB + 200
    else:
        salarioB = salarioB + 300
else:
    if tempo <= 3:
        salarioB = salarioB + 230
    elif tempo <= 6:  #elif tempo>3 and tempo<=6
        salarioB = salarioB + 330
    else:
        salarioB = salarioB + 350
print("O salario base acrescido da gratificação é: ", salarioB)
