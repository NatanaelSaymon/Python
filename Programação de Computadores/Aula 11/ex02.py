# Exemplo 2
# Facaum programa em python que solicite ao usuario, enquanto o mesmo desejar 
nomes=[]
for cont in range(5):
    nomes.append(input("Digite um nome"))

indice=int(input("Digite um indice"))
if indice >= 0 and indice < len(nomes):
    print('Nome ', nomes[indice])
else:
    print('Indice invalido')
