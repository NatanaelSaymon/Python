# ESTRUTURA DE CONTROLE

# CONDIÇÕES ANINHADAS

nome = str(input('Por favor digite o seu nome: '))
if nome == 'Natanael':
    print('Que nome bonito voce tem!!')
elif nome == 'Mateus' or nome == 'Pedro' or nome == 'João':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Any Luiza Isabel Suellen':
    print('Que belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
