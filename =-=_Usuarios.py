# ------------------------------------------------------------------------------
# Crie u programa interativo de usuario e senha.
# O programa irá perguntar o que o usuario deseja fazer da seguite maneira


# ------------------------------------------------------------------------------
# Variaveis de escolha de opções
# "opcao", "op"


# ------------------------------------------------------------------------------
# As variaveis "cafe, leite" sao usuadas nas opcoes "1, 3, 4, 5"


# ------------------------------------------------------------------------------
# As variaveis da opcao 1
# "usuarU, usartS, reposta"


# ------------------------------------------------------------------------------
# As variaveis da opcao 2
# "vU, vS", "verificandoU, trocaU", "verficandoS, trocaS", "troca"


# ------------------------------------------------------------------------------
# A variavel da opcao 3
# "excluirU"


# ------------------------------------------------------------------------------
# As variaveis da opcao 4
# "u, s"


# ------------------------------------------------------------------------------
# Import serve para dar uma impressão de "Demora"
import time


# ------------------------------------------------------------------------------
from array import *

# A variaveis "Usuário e senha" são as listas
usuario = [[], []]


# ------------------------------------------------------------------------------
# A opção começa com "0" para o contador iniciar com nada
opcao = 0


# ------------------------------------------------------------------------------
# Titulo
centro = 'Banco de Dados simples'
print('===' * 35)
print(centro.rjust(60))
print('===' * 35)

# Escolhas das opção para os usuários
while opcao != 5:
    print('''[ 1 ] incluir usuario e senha.
[ 2 ] Editar um usuário e senha, para isso é necessario tem usuários cadastrados.
[ 3 ] Excluir usuario, para isso é necessario tem usuários cadastrados.
[ 4 ] Verficar nome e senha do usuario estão corretos, para isso é necessario tem usuarios cadastrados.
[ 5 ] Encerrar o Programa.''')
    print('---' * 35)
    opcao = int(input('Qual e a opção: '))
# Opção "1"
    if opcao == 1:
        print('Aguarde...')
        time.sleep(0.8)
        print('---' * 35)
        resposta = 'S'
        while resposta == 'S':
            usuarU = str(input('Qual e o usuário que voçê gostaria de adicionar: ')).strip().capitalize()
            usuarS = input('Qual e senha do usuário adicionado: ').strip()
            usuario[0].append(usuarU)
            usuario[1].append(usuarS)
            resposta = str(input('Quer cadastrar mais [s/n]: ')).strip().upper()[0]
            while resposta not in 'SN':
                resposta = str(input('Dados Inválidos. Por favor, informe com S ou N: ')).strip().upper()[0]
        for cafe, leite in zip(usuario[0], usuario[1]):
            print('---' * 35)
            print('Usuário {} adicionado, sua senha: {}'.format(cafe, leite))
            print('Usuário inserido com sucesso')
        print('===' * 35)
        print(centro.rjust(60))
        print('===' * 35)
        time.sleep(0.8)
# Opção "2"
    if opcao == 2:
        print('Preparando Login ...')
        time.sleep(0.9)
        vU = str(input('Digite um usuário cadastrado para fazer o login: ')).strip()
        vS = input('Digite a senha desse usuário: ').strip()
        usuario[0].count(vU)
        usuario[1].count(vS)
        print('---' * 35)
        if vU in usuario[0]:
            print('Fazendo Login')
            if vS in usuario[1]:
                print('Aguarde... :)')
                time.sleep(2)
                print('---' * 35)
                print('''
[ 1 ] Para trocar o Usuario.
[ 2 ] Para trocar Senha.
                ''')
                op = int(input('Qual e a Opçâo: '))
                print('Processando Dados...')
                time.sleep(0.6)
                if op == 1:
                    verficandoU = str(input('Qual e o usuário atual: ')).strip()
                    trocaU = str(input('Qual e o novo usuário: ')).strip().capitalize()
                    troca = usuario[0].index(verficandoU)
                    usuario[0][troca] = trocaU
                    print('Seu usuario foi alterado com sucesso')
                elif op == 2:
                    verficandoS = input('Qual e a senha antiga desse usuario: ').strip()
                    trocaS = input('Qual e a nova senha: ').strip()
                    troca = usuario[1].index(verficandoS)
                    usuario[1][troca] = trocaS
                    print('Sua senha foi alterada com sucesso')
        elif vU not in usuario[0]:
            print('Usuario não cadastrado')
            print('---' * 35)
# Opção "3"
    if opcao == 3:
        print('Processando Dados...')
        time.sleep(1.5)
        for cafe in zip(usuario[0],):
            print('---' * 35)
            print('Usuário {}'.format(cafe))
            print('---' * 35)
        print('---' * 35)
        excluirU = str(input('Qual e o usuario que voçê quer excluir: ')).strip()
        usuario[0].remove(excluirU)
        print('Usuário {} foi excluido com sucesso'.format(excluirU))
        print('---' * 35)
# Opção "4"
    if opcao == 4:
        print('Processando Dados...')
        time.sleep(0.6)
        for cafe in zip(usuario[0]):
            print('---' * 35)
            print('Usuário {}.'.format(cafe))
        print('---' * 35)
        u = str(input('Qual usuário voçê quer verficar: ')).strip()
        s = input('Qual e a senha desse usuário: ').strip()
        usuario[0].count(u)
        usuario[1].count(s)
        print('---' * 35)
        if u in usuario[0]:
            print('O usuário {}'.format(u))
            if s not in usuario[1]:
                print('Mas essa nao a senha dele :)')
                print('---' * 35)
            if s in usuario[1]:
                print('senha estao cadastrado :)')
                print('---' * 35)
        elif u not in usuario[0]:
            print('Usuario não esta cadastrado')
            print('---' * 35)
            if s not in usuario[1]:
                print('Cadastra-se no meu programas :)')
                print('---' * 35)
# Opção "5"
    if opcao == 5:
        print('---' * 35)
        print('Processando Todos os Dados')
        print('---' * 35)
        time.sleep(2)
        print('Todos os Usuários Cadastrados e suas Senhas')
        for cafe, leite in zip(usuario[0], usuario[1]):
            print('   ' * 35)
            print('---' * 35)
            print('Usuário informado {}, sua senha: {}'.format(cafe, leite))
        print('---' * 35)
        # Encerrando o Programa
        print('Encerrando...')
        time.sleep(3)
        break
print('Fim do Programa! Obrigado!!')
