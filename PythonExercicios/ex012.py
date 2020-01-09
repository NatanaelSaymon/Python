# Faca um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
# Ex: 10 = 100%
# Ex 10 * 5 / 100 <- Estrutura de procentagem. 5 é a quantidade de desconto ou 5 porcento de 100


preço = float(input('Digite o preço do produto: R$'))
novop = preço - (preço * 5 / 100)
print('O produto que custava R${}, na promoção com 5% de desconto vai custar R${}'.format(preço, novop))


