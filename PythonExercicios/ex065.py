# CRIE UM PROGRAMA QUE LEIA VARIOS NUMEROS INTEIROS PELO TECLADO. NO FINAL DA EXECUÇÃO, MOSTRE A MEDIA ENTRE TODOS OS VALORES
# E QUAL FOI O MAIOR E O MENOR VALORES LIDOS. O PROGRAMA DEVE PERGUNTAR AO USUARIO SE ELE QUER OU NÃO CONTINUAR A DIGITAR VALORES.

resp = 'Ss'
soma = 0
media = 0
quant = 0
maior = 0
menor = 0
while resp in 'Ss':
    num = int(input('Digite um valor: '))
    soma = soma + num
    quant = quant + 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} numeros e a media entre eles foi de {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
