# Faca um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

a = input('Digite algo: ')
print('O tipo primitivo desse valor é:', type(a))
print('Tem espaços? ', a.isspace())
print('É numero', a.isnumeric())
print('É alfabetico?', a.isalpha())
print('É numerico?', a.isalnum())
print('Está em maiusculas?', a.isupper())
print('Está em minusculas?', a.islower())