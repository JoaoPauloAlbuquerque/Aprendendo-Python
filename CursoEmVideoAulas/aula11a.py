# PADRÃO DE USAR CORES NO TERMINAL:
# \033[STYLE; TEXTO; BANCKGROUNDm

# STYLE:
# 0 = none
# 1 = bold
# 4 = undergroud
# 7 - negative

# TEXTO:
# 30 = preto
# 31 = vermelho
# 32 = verde
# 33 = amarelo
# 34 = azul
# 34 = magenta
# 36 = ciano
# 37 = cinza
# 97 = branco

# BACKGROUND:
# 40 = preto
# 41 = vermelho
# 42 = verde
# 43 = amarelo
# 44 = azul
# 44 = magenta
# 46 = ciano
# 47 = cinza
# 107 = branco

print('\033[0;34;47mOlá mundo!\033[m')  # Este "\033[m" no final reseta a configuração no final do texto

a = str('João Paulo')
corFonteVermelha = str('\033[1;31m')  # criando uma variável para armazenar a cor
print(f'{corFonteVermelha}{a}')

# Armazenando cores em uma lista
coresFonte = {
    'limpa': '\033[m',
    'azul': '\033[34m',
    'vermelho': '\033[31m'
}
print(f'{coresFonte["azul"]}Azul')
