#Faça um programa em Python que obtenha o valor de uma
#compra, calcular e mostrar o valor da compra considerando o
#desconto, conforme descrito abaixo:
#para compras acima de R$ 200 a loja dá um desconto de 20%
#para as abaixo disso não tem desconto, mostre o valor da compra.

compra = float(input('Informa o valor da sua compra: '))
if compra > 200:
    des = compra - (compra * 20 / 100)
    print('O valor da sua compra com 20% de desconto foi de R${}'.format(des))
else:
    print('O valor da sua compra foi baixo e não terá desconto.')
