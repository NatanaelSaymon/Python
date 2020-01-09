#Elabore um programa em Python que implemente uma
#calculadora com as funções de somar, subtrair, multiplicar e
#dividir. O programa deverá solicitar ao usuário os dois
#valores, e perguntar qual a operação pretendida (‘+’, ‘-‘ , ‘*’
#ou ‘/’ ) e a seguir calcular e mostrar o resultado.

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
operacao = str(input('Qual operação voce deseja realizar: +, -, *, /: '))
if operacao == "+":
    print('A soma dos valores é: {}'.format(n1 + n2))
elif operacao == "-":
    print('A subtracao dos valores é: {}'.format(n1 - n2))
elif operacao == "*":
    print('a multiplicação dos valores é: {}'.format(n1 * n2))
elif opercao == "/":
    print('A divisão dos valores é: {}'.format(n1 / n2))