# Escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros.

# km hm dam m dm cm mm

media = float(input('Digite uma distância em metros: '))
cm = media * 100
mm = media * 1000
km = media * 0.001
print('A media de {}m corresponde a {}cm e {}mm e {}km'.format(media, cm, mm, km))