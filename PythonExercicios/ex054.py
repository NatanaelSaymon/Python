# CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE 7 PESSOAS. NO FINAL, MOSTRE QUANTAS PESSOAS AINDA NÃO ATINGIRAM
# A MAIORIDADE E QUANTAS JÁ SÃO MAIORES.
totmenor = 0
totmaior = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}ª nasceu? '.format(c)))
    idade = 2018 - ano
    if idade <= 17:
        totmenor += 1
    else:
        totmaior += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(totmaior))
print('E tivemos também {} pessoas menores de idade.'.format(totmenor))