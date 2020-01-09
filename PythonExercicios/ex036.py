# Escreva um programa para aprovar o emprestimo bancario para a compra de ua casa. Pergunte o valor da casa, o salario do comprador
# e em quantos anos ele vai pagar. A prestação mensal, não pode exceder 30% do salario ou então o emprestimo erá negado.

casa = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
anos = int(input('Quantos anos de financiamento: '))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de RS{:.2f} em {} anos.'.format(casa, anos), end=' ')
print('A prestação será de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('Emprestimo CONCEDIDO!!')
else:
    print('Emprestimo NEGADO!!')