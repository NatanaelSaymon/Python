#Exemplo 3 - Volume do tronco de um cone

import math

#obtem dados - Entrada de dados
h = float(input("Digite a altura do tronco do cone: "))
Rmaior = float(input("Digite o valor do maior raio: "))
Rmenor = float(input("Digite o valor do menor raio: "))

#processamento
volume = (math.pi * h)/3*(math.pow(Rmaior,2) + Rmaior * Rmenor + math.pow(Rmenor,2))

#exibe resultado
print("O volume é: ",volume)
