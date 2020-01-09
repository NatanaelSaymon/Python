nota1 = float(input("Digite a Primeira nota: "))
nota2 = float(input("Digite a Segunda nota: "))
freq = float(input("Qual a media de frequencia: "))
media = (nota1 + nota2) / 2
if freq >=75:
    if media >=6:
        print("Aprovado, sua media foi:", media)

    else:
        print("Reprovado por nota. Sua media foi", media)

else:
    print("Reprovado por falta IDIOTA")
      
