# Nessa aula, vamos aprender operações com string no python. As principais operações que vamos aprender são
# o FATIAMENTO de string, analise com len(), count(), find(), tranformações com replace(), upper(), lower(),
# capitalize(), title(), strip(), junção com join().

# Fatiamento : conseguir pegar pedaços dela.

# Analise: analisa uma strng, saber qual o tamanho, com letra ela começa, etc.
#       Função len(frase): significa comprimento da frase.
#       Função frase.count('o'): conta quantas vezes aparece a letra 'o' minuscula.
#              frase.count('o', 0, 13): conta quantas vezes o 'o' aparece da posição 0 ate o 13.
#       Funçao frase.find('deo'): conta quantas vezes ele encontrou a palavra 'deo'.

# Transformações: consegue mudar uma lista atraves de metodos.
#       Função frase.replace('python', 'android'): troca a palavra 'python' por 'android'.
#       Função frase.upper(): Significa para cima. Pega todas as letras da frase e coloca em 'maiusculo'
#       Função frase.lower(): Significa para baixo. Pega todas a letras da frase e coloca em minuscula.
#       Função frase.captalize(): Significa joga todos os caracteres para minusculo e somente o primeiro caracter fica em maiusculo.
#       Função frase.title(): analisa quantas palavras tem a frase e coloca todas as palavras com sua primeira letra em 'maiusculo'.
#       Função frase.strip(): remove todos os espaços inuteis no inicio e no fim da string.
#              frase.rstrip(): remove somente os espaços da direita.
#              frase.lstrip(): remove somente os espaços da esquerda.

#Divisão: divide uma string.
#       Função frase.split(): ocorrer uma divisão dentro da string considerando seus espaços. Dividi uma string em uma lista, onde cada elemento vai ser
#       separado pelo seu sliptador
#       Função join(): junta uma coisa na outra. Ex: '-'.join(frase) -> Significa junta todos os elementos separados e colocar '-' para separar

#"CURSO EM VIDEO PYTHON" <-  Cadeia de caracteres


frase = 'Curso em Video Python'
print(frase[1:15:2])
print(frase.count('o'))
print(len(frase))
print(frase.upper().count('O')) # <- combinando upper com count (joga todas as letras para maiuscula e conta quantos 'O' maiusculos tem.
print(frase.replace('Python', 'Android'))
print(frase.split()) # <- splita a frase

print("""coloque aqui o texto""") # <- usando 3 aspas voce pode imprimir na tela o txto em sua forma original.