#Crie um programa que leia o nome de uma cidade diga se ela comça ou não com o nome 'SANTO'.

cid = str(input('Em que cidade voce nasceu? ')).strip() # strip elimina os espaços
print(cid[:5].upper() == 'SANTO') #upper joga tudo para maiusculo.