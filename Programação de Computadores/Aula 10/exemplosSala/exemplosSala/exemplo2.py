#Exemplo 2 - Funções matemáticas

import math  #importa módulo matemático

#obtem valores
v1 = float(input("Digite um número: "))
v2 = int(input("Digite outro número: "))

#utiliza algumas funções matemáticas
print("Valor truncado: ",math.trunc(v1))
print("Arredonda para cima: ", math.ceil(v1))
print("Fatorial: ",math.factorial(v2))
print("Valor de pi: ",math.pi)
