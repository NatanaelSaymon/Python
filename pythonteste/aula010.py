# ESTRUTURA CONDICIONAL (PARTE1)
# Nessa aula, vamos aprender como utilizar estruturas condicionais simples e compostas nos seus programas em python.
# Veja como aplicar os comandos if: e else: no python.

nome = str(input('Digite o seu nome completo: ')).upper().strip()
if nome == 'NATANAEL SAYMON':
    print('Olá meu querido, voce esta de volta! É muito bom vê-lo novamente.')
else:
    print('Olá, seja bem vindo {}'.format(nome))
print('Fim')