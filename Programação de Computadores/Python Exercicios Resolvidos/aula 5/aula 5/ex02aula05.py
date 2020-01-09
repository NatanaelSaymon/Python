#Escreva um programa em Python que solicite ao usuário os
#valores de três contas de consumo (p.ex. água, luz e telefone) e
#o valor de seu salário. Verifique se o salário é suficiente para
#pagar as três contas, caso não seja apresente a mensagem
#“Salário insuficiente!”. Caso seja, apresente o valor que restou
#do salário após pagar as contas.

agua=float(input("Digite o valor da conta de água: R$ "))
luz=float(input("Digite o valor da conta de Luz: R$ "))
tel=float(input("Digite o valor da conta de telefone: R$ "))
salario=float(input("Digite o valor do salario: R$ "))
sm= agua + luz + tel
sb= salario - sm
if salario >= sm:
    print("Seu salario restante é R$", sb)
else:
    print("Salario insuficiente!")