# CORES NO TERMINAL
# Nessau aula, vamos aprender como utilizar os codigos de escape sequence ANSI para configurar cores para os seus programas em python.
# Veja como utilizar o codigo \033[m com todas as suas principais possibilidades.

# Style: estilo da letra.
# Text: cor da letra.
# Back: cor do fundo.

# Style : 0 none, 1 bold, 4 underline 'sublinhado', 7 negative 'inverte'
# Text: 30 branco, 31 vermelho, 32 verde, 33 amarelo, 34 azul, 35 lilas, 36 verde, 37 cinza.
# Background: 40 branco, 41 vermelho, 42 verde, 43 amarelo, 44 azul, 45 lilas, 46 verde, 47 cinza.
# ex: \033[0;33;44m

#PRATICA!!
print('\033[1;30;44mOlá, Mundo!\033[m')
print(' ')
print('\033[7;30mNatanael Saymon\033[m')