# Faça um programa em Python que leia um valor n,
# inteiro e positivo, calcule e mostre a seguinte soma:
# S = 1 + 1/2 + 1/3 + 1/4 +...+ 1/n

n = int(input("Digite o valor de n: "))

soma = 0

i = 1 + 1/2 + 1/3 + 1/4
while i <= n:
    soma = soma + i
    i = i + 1

print("A soma dos", n, "primeiros inteiros positivos é", soma)
