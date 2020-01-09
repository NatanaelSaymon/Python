# PRIMEIRO E ULTIMO NOME
# Faca um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.

n = str(input('Digite seu nome completo: ')).strip().upper()
nome = n.split()
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu ultimo nome é: {}'.format(nome[len(nome)-1]))

