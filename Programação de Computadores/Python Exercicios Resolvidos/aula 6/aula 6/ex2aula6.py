#Crie um programa em Python que solicite ao usuário o peso e
#a altura e calcule o Índice de Massa Corpórea
#IMC= peso/altura2
#E mostre em qual categoria o usuário se encontra, conforme a
#tabela abaixo:
pe = float(input("Informe o sei peso: "))
alt = float(input("informe a sua altura: "))
imc = pe / alt ** 2
print(imc)
if imc <= 20:
    print("seu imc esta abaixo do normal")
elif imc >= 20 and imc < 25:
    print('Seu imc esta normal')
elif imc >= 25 and imc < 30:
    print('voê está com sobrepeso')
elif imc >= 30 and imc < 40:
    print('você está obeso')
elif imc >= 40:
    print('você está com obesidade mórmida')
else:
     print("não tem resultado")
