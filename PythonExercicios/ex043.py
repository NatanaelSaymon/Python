# Elabore um programa que calcule o valor a ser pago por um produto considerando o seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO
# Á vista dinheiro/cheque: 10% de desconto
# A vista no cartão: 5% de desconto
# Em até 2x vezes do no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format(' LOJAS SAYTECH '))
preco = float(input('Informe o valor das suas compras: R$'))
print('''FORMA DE PAGAMENTO
[ 1 ] A VISTA DINHEIRO/CHEQUE
[ 2 ] A VISTA NO CARTÃO
[ 3 ] EM 2X NO CARTÃO
[ 4 ] 3X OU MAIS NO CARTÃO''')
opcao = int(input('Qual é a opção: '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print('Sua compro de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas: '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(totparc, parcela))
    print('Sua compra de RS{:.2f} vai custar R${:.2f} no final.'.format(preco, total))
else:
    total = preco
    print('\033[1;31mOPÇÃO INVALIDA DE PAGAMENTO. Tente novamente!\033[m')

