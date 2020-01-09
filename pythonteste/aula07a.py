# Nessa aula, vamos aprender quais são os operadores artimeticos do python e tbm sua ordem de precedencia dentro ded expressões matematicas.
# Veja como funcionam os operadores de adição, subtração, multiplicaçao, divisão, exponenciação e quociente na linguagem python.
# + adição
# - subitração
# * multiplicação
# / divisão
#
#** potencia ou expenenciação
# // divisão inteira
# % resto da divisão

# Ordem de precedencia
# 1 ()
# 2 **
# 3 * / // %
# 4 + -

# end('') não quebra a linha de um print para o outro

# \n significa quebra de linha


n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma dos valores é {}'.format(s))
print('A multiplicação dos valores é {}'.format(m))
print('A divisão dos valores é {:.2f}'.format(d))
print('A divisão inteira dos valores é {}'.format(di))
print('A potencia dos valores é {}'.format(e))