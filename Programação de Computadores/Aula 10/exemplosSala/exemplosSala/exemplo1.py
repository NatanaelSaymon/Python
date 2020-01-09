#Exemplo 1 - Aula 04 - Calculadora

num1 = input("Digite o primeiro valor: ") #Obtem valor via teclado
num1 = float(num1)                          #Converte para float (número com casas decimais)
num2 = float(input("Digite o segundo valor: "))  #Obtem valor e converte para float 
#Operadores aritméticos
print("A soma é: ", (num1 + num2))
print("A subtração é: ",(num1 - num2))
print("A multiplicação é: ",(num1 * num2))
print("A divisão é: ",(num1 / num2))
print("A divisão inteira é: ",(num1 // num2))
print("O resto da divisão é: ",(num1 % num2))
print("A exponenciação é: ",(num1 ** num2))
