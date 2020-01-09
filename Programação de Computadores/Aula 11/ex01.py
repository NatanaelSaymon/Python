#Exemplo 1 - Conceitos basicos de lista

#Criação da lista

#Aramazena valores na lista

nomes =[] #ou nome = list()
for i in range(5):
    n = input("Digite um nome: ")
    nomes.append(n) #Adiciona no final da lista
print(nomes) #Mostra valores da lista

print(len(nomes),"Elementos") #Quantidade de elementos da lista

nomes.remove("natan") #Exclui um elemento da lista
print(nomes)
