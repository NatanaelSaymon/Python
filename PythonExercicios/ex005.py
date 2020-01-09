# Faca um programa que leia um nuemro inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input('Digite um numero: '))
s = num - 1
m = num + 1
print('Valor digitado é {}. Seu antecessor é {} e seu sucessor é {}'.format(num, s, m))