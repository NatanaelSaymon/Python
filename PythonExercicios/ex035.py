#ANALISANDO TRIANGULO
#Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou não formar um triangulo.


print('-=' * 15)
print('Analisador de triangulos')
print('-=' * 15)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmento acimna "PODEM FORMAR UM TRIANGULO!!"')
else:
    print('Os segmentos acima "NÃO PODEM FORMAR UM TRIANGULO!!"')