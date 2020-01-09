# Crie um programa que leia duas notas de uma aluno e calcule a sua media
# mostrando uma mensagem no final, de acordo com a media atingida:

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('Você está REPROVADO!')
elif m > 5 and m < 6.9:
    print('Você está de RECUPERAÇÃO')
elif m >= 7:
    print('Você está APROVADO! Parabens!')
