# Escreva um programa que converta um temperatura digitando em graus celsius e converta para graus Fahrenheit

Celsius = float(input('Informe a temperatura em ºC: '))
F = ((9 * Celsius) / 5) + 32
print('A temperatura de {}°C corresponde a {}°F'.format(Celsius, F))