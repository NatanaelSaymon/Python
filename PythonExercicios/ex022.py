# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiusculas e minusculas;
# Quantas letras ao todo (sem considerar espaços);
# Quantas letras tem o primeiro nome;

nome = str(input('Digite o seu nome completo: '))
print('Analisando o seu nome...')
print('Seu nome em maiusculo é {}'.format(nome.upper()))
print('Seu nome em minusculo é{}'.format(nome.lower()))
print('Seu nome completo tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))