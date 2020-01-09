# Exemplo 3 - quantidade indeterminada de itens

n = list()
r = 's'

while r=='s' or r=='S':
    n.append(float(input('Digite um valor: ')))
    r = input('Deseja continuar ? (S/N)')
s = 0 #acumulador
for cont in n:
    s = s + cont #soma valores
media = s/len(n) #calculo da media

#quantidade de numeros acima da media
qtde = 0 #contador
for cont in n:
    if cont > media:
        qtde = qtde + 1
print('Media = ', media, '/n Valores acima da media: ', qtde)
