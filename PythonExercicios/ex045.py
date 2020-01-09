# Refaca o DESAFIO 35 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:
# Equilatero: todos os lados iguais
# Isosceles: dois lados iguais
# Escaleno: todos os lados diferentes

t1 = int(input('Digite o primeiro segmento: '))
t2 = int(input('Digite o segundo segmento: '))
t3 = int(input('Digite o segundo segmento: '))

if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print('Os segmentos acima podem formar um triangulo ', end='')
    if t1 == t2 and t3 == t1:
        print('EQUILATERO!')
    elif t1 != t2 and t2 != t3 and t3 != t1:
        print('ESCALENO!')
    else:
        print('ISOSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIANGULO!')