print ("----------------------------")
print ("    Hotel Qualquer um       ")
print ("----------------------------")

qntDiaria = int(input("Digite a quantidade de diaria: "))
tipo = input("Digite  o tipo de Hospedagem: \nS - Simples \nD - Duplo \nT - Tripo \n")

if tipo=="S" or tipo=="s":
    print("Valor a pagar", (qntDaria*255.5))
else:
    if tipo=="D" or tipo=="d":
        print("Valor a pagar", (qntDiaria*305.5))
    
    else:
        if tipo=="T" or tipo=="t":
            print("Valor a pagar", (qntDiaria*360.5))
        else:
            print("Tipo de hospedagem invalida")
        
