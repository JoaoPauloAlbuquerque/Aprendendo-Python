# Faça um minissistema que utilize o interactive help do python. O usuário vai
# digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM'
# o programa se encerrará.
# OBS: use cores.
from time import sleep
cores = {
    'none': '\033[m',
    'ciano': '\033[1;97;46m',
    'branco': '\033[1;30;107m',
    'cinza': '\033[1;97;47m',
}


def titulo(msg, cor):
    sleep(0.5)
    tam = len(msg) + 4
    print(cor, end='')
    print('~' * tam)
    print(f'{msg:^{tam}}')
    print('~' * tam)
    print(cores['none'], end='')
    sleep(0.5)


while True:
    c = str(input('Função ou Biblioteca >>> '))
    if c.upper() == 'FIM':
        break
    titulo(f"Acessando manual do '{c}'", cores['ciano'])
    print(cores["branco"], end='')
    print(help(c))
    print(cores["none"], end='')
    titulo(f'SISTEMA DE AJUDA PyHELP', cores['cinza'])
