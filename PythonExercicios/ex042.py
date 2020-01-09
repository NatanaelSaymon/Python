# Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre
# status, de acordo com a tabela abaixo:

print('-=' * 20)
print('\033[1;31mIndice de Massa Corporal\033[m')
print('-=' * 20)
print('\033[1;31mAbaixo de 18.5: Abaixo do peso.\033[m')
print('\033[1;31mEntre 18.5 e 25: Peso Ideal\033[m')
print('\033[1;31m25 até 30: Sobrepeso\033[m')
print('\033[1;31m30 até 40: Obesidade\033[m')
print('\033[1;31mAcima de 40: Obesidade morbida.\033[m')
print('-=' * 20)
peso = float(input('Qual é o seu peso: (Kg) '))
alt = float(input('Qual a sua altura? (m) '))
imc = peso / (alt ** 2)
print('O seu IMC é de: {}'.format(imc))
if imc < 18.5:
    print('Voce está ABAIXO DO PESO normal!')
elif imc >= 18.5 and imc <= 25:
    print('Parabens! Voce está com o PESO NORMAL.')
elif imc > 25 <= 30:
    print('Você está com SOBREPESO!')
elif imc > 30 <= 40:
    print('Você está com OBESIDADE! Cuidado!')
elif imc > 40:
    print('Você com OBESIDADE MÓRBIDA Cuidado!')





